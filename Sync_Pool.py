from Sync_Filter import Sync_Filter
import subprocess
from distutils.dir_util import copy_tree
import utils
import re
class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        self._dst_pool_path = path/'dst'
        self._src_pool_path = path/'src'
        self._src_temp_path = path / 'src_temp'
        self._dst_temp_path = path / 'dst_temp'
        self.clean_pool()
        pass
    
    def filter_dst_pool(self, filter : Sync_Filter):
        filter.apply_filter(self._dst_pool_path) 
        pass

    def filter_src_pool(self, filter : Sync_Filter):
        filter.apply_filter(self._src_pool_path) 
        pass
    

    def include_src_repo_info(self): #must test
        dot_git_dir_path = str(self._src_temp_path / '.git')
        info_dst_path = str(self._src_pool_path)
        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass

    def exclude_src_repo_info(self): #must test
        dot_git_dir_path = str(self._src_pool_path / '.git')
        info_dst_path = str(self._src_temp_path)
        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass

    def include_dst_repo_info(self): #must test
        dot_git_dir_path = str(self._dst_temp_path)
        info_dst_path = str(self._dst_pool_path / '.git')
        print('include from ' + dot_git_dir_path +' to ' + info_dst_path )

        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass

    def exclude_dst_repo_info(self): #must test
        dot_git_dir_path = str(self._dst_pool_path / '.git' )

        info_dst_path = str(self._dst_temp_path )

        print('exclude from ' + dot_git_dir_path +' to ' + info_dst_path )
        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass
    
    
    def clone_src(self, src_repo_url):
        subprocess.run(['git', 'clone',  src_repo_url, self._src_pool_path], shell=True)
        pass

    def clone_dst(self, dst_repo_url):
        subprocess.run(['git', 'clone',  dst_repo_url, self._dst_pool_path], shell=True)
        pass


    

    
    def clone_src_dst(self, src_repo_url, dst_repo_url, branch_name):
        if utils.branch_exists(dst_repo_url, branch_name):
            print('Branch: "'+branch_name+'" exists in destination repository.\n')
            #clone branch of repositories src,dst -> pool
            subprocess.run(['git', 'clone', '--branch', branch_name, dst_repo_url, self._dst_pool_path], shell=True)
            subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=True)
            
        else:
            print('Branch: "'+branch_name+'" does not exist in destination repository.\n')

            subprocess.run(['git', 'clone',  dst_repo_url, self._dst_pool_path], shell=True)
            subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=True)
            self.push_branch(self._dst_pool_path, branch_name)
    
    def local_merge(self):
        # copy subdirectory src -> dst
        from_directory = str(self._src_pool_path)
        to_directory = str(self._dst_pool_path)
        utils.rm_dir(self._src_pool_path/'.git')  # to be replaced with the include and exclude functionality 
        copy_tree(from_directory, to_directory) # to be replaced with the include and exclude functionality 

        #subprocess.run(['git', '-C', self._dst_pool_path, 'remote', 'set-url', 'origin', dst_repo_url], shell=True)

    def merge_to_dst(self): # to delete and use push_to_dst instead
        subprocess.run(['git', '-C',self._dst_pool_path, 'add', '.'], shell=True)
        subprocess.run(['git', '-C', self._dst_pool_path, 'commit', '-m', 'Merge from: internal repo' ], shell=True)
        subprocess.run(['git', '-C',self._dst_pool_path, 'push' , 'origin'], shell=True)
        pass

    def push_to_src(self):
        """ 
        Function to push (add ., commit and push) changes in local src repository to remote src repository using push_to_remote function from utils class.
        """
        
        utils.push_to_remote(self._src_pool_path)
        pass

    def push_to_dst(self):
        """ 
        Function to push (add ., commit and push) changes in local dst repository to remote dst repository using push_to_remote function from utils class.
        """
        
        utils.push_to_remote(self._dst_pool_path)
        pass

    def git_new_branches(self, src_repo_url): # make it more efficient 
        new_branches = []
        res = subprocess.check_output(['git', '-C', self._dst_pool_path, 'ls-remote'], shell=True)
        a = "refs/heads/"
        b = "\n"
        branches = re.findall(rf'{a}(.*?){b}', res.decode('utf-8'))
        for branch_name in branches:
            if not(utils.branch_exists(src_repo_url, branch_name)) and len(branch_name) > 0:
                new_branches.append(branch_name)
        return new_branches
    

    def push_branch(self, local_repo, branch_name):
        subprocess.run(['git', '-C', local_repo,'checkout', '-b', branch_name], shell=True)
        subprocess.run(['git', '-C', local_repo, 'push', '--set-upstream', 'origin', branch_name], shell=True)
        pass
    

    def pull_new_branches(self, src_repo_url):  # bug here. critical segment
        new_branches = self.git_new_branches(src_repo_url)
        for new_branch in new_branches:
            self.push_branch(self._src_pool_path, new_branch)
            #copy content here to current branch.
            subprocess.run(['git', '-C', self._dst_pool_path, 'checkout', new_branch], shell=True)
            self.exclude_dst_repo_info()
            utils.copy_dir(self._dst_pool_path, self._src_pool_path)
            self.include_dst_repo_info()
            self.push_to_src()


    def clean_pool(self): 
        print('Cleaning pool...')
        utils.rm_dir(self._pool_path)
        pass


