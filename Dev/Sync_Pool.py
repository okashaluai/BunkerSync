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
        """This function applies a Sync_Filter object on the destination pool path.

        Args:
            filter (Sync_Filter): An object of the Sync_Filter class that contains the filter rules to be applied on the destination pool.
        """
        if filter is None:
            return
        filter.apply_filter(self._dst_pool_path) 
        pass

    def filter_src_pool(self, filter : Sync_Filter):
        """This function applies a Sync_Filter object on the source pool path.

        Args:
            filter (Sync_Filter): An object of the Sync_Filter class that contains the filter rules to be applied on the source pool.
        """
        if filter is None:
            return
        filter.apply_filter(self._src_pool_path) 
        pass
    

    def include_src_repo_info(self): 
        """This function includes the repository information from the source temporary directory to the source pool directory.
        """
        dot_git_dir_path = str(self._src_temp_path )
        info_dst_path = str(self._src_pool_path/ '.git')
        print('include from ' + dot_git_dir_path +' to ' + info_dst_path )
        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass

    def exclude_src_repo_info(self): 
        """This function excludes the repository information from the source pool directory and moves it to the source temporary directory.
        """        
        dot_git_dir_path = str(self._src_pool_path / '.git')
        info_dst_path = str(self._src_temp_path)
        print('exclude from ' + dot_git_dir_path +' to ' + info_dst_path )
        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass

    def include_dst_repo_info(self): 
        """This function includes the repository information from the destination temporary directory to the destination pool directory.
        """
        dot_git_dir_path = str(self._dst_temp_path)
        info_dst_path = str(self._dst_pool_path / '.git')
        print('include from ' + dot_git_dir_path +' to ' + info_dst_path )

        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass

    def exclude_dst_repo_info(self): 
        """This function excludes the repository information from the destination pool directory and moves it to the destination temporary directory.
        """
        dot_git_dir_path = str(self._dst_pool_path / '.git' )
        info_dst_path = str(self._dst_temp_path )
        print('exclude from ' + dot_git_dir_path +' to ' + info_dst_path )
        utils.move_dir(dot_git_dir_path, info_dst_path)
        pass
    
    
    def clone_src(self, src_repo_url):
        """This function clones the source repository from the given URL and saves it to the source pool directory.

        Args:
            src_repo_url (str): The URL of the source repository.
        """
        subprocess.run(['git', 'clone',  src_repo_url, self._src_pool_path], shell=False)
        pass

    def clone_dst(self, dst_repo_url):
        """This function clones the destination repository from the given URL and saves it to the destination pool directory.

        Args:
            dst_repo_url (str): The URL of the destination repository.
        """
        subprocess.run(['git', 'clone',  dst_repo_url, self._dst_pool_path], shell=False)
        pass

    def clone_dst_branch(self, dst_repo_url, branch_name):            
        subprocess.run(['git', 'clone', '--branch', branch_name, dst_repo_url, self._dst_pool_path], shell=False)
        pass
    
    def clone_src_branch(self, src_repo_url, branch_name):
        subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=False)
        pass

    def clone_src_dst(self, src_repo_url, dst_repo_url, internal_branch_name, external_branch_name, external_branch_base):
        """_summary_

        Args:
            src_repo_url (_type_): _description_
            dst_repo_url (_type_): _description_
            branch_name (_type_): _description_
        """
        if utils.check_branch_exists(dst_repo_url, external_branch_name):
            print('Branch: "'+external_branch_name+'" exists in destination repository.\n')
            #clone branch of repositories src,dst -> pool
            self.clone_src_branch(src_repo_url, internal_branch_name)
            self.clone_dst_branch(dst_repo_url, external_branch_name)
        else:
            print('Branch: "'+external_branch_name+'" does not exist in destination repository.\n')
            self.clone_dst(dst_repo_url)
            self.clone_src_branch(src_repo_url, internal_branch_name)
            # subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=False)
            self.push_branch(self._dst_pool_path, external_branch_name, external_branch_base)
    
    def local_merge(self):
        """This function performs a local merge of the changes from the source repository to the destination repository. 
           It copies the subdirectory from the source pool to the destination pool directory.
        """
        # copy subdirectory src -> dst
        from_directory = str(self._src_pool_path)
        to_directory = str(self._dst_pool_path)
        # utils.rm_dir(self._src_pool_path/'.git')  # to be replaced with the include and exclude functionality 
        # copy_tree(from_directory, to_directory) # to be replaced with the include and exclude functionality 
        self.exclude_src_repo_info()
        utils.copy_dir(from_directory, to_directory)

    def push_to_src(self):
        """ 
        This function pushes (add ., commit and push) changes in local src repository to remote src repository using push_to_remote function from utils class.
        """
        
        utils.push_to_remote(self._src_pool_path)
        pass

    def push_to_dst(self):
        """ 
        This function pushes (add ., commit and push) changes in local dst repository to remote dst repository using push_to_remote function from utils class.
        """
        
        utils.push_to_remote(self._dst_pool_path)
        pass

    def git_new_branches(self, src_repo_url, prefix): # make it more efficient 
        """_summary_

        Args:
            src_repo_url (_type_): _description_

        Returns:
            _type_: _description_
        """
        new_branches = []        
        
        # res = subprocess.check_output(['git', '-C', self._dst_pool_path, 'ls-remote'], shell=False)
        res = subprocess.run(['git', '-C', self._dst_pool_path, 'ls-remote'], shell=False, capture_output=True).stdout
        a = "refs/heads/"+prefix
        b = "\n"
        branches = re.findall(rf'{a}(.*?){b}', res.decode('utf-8'))
        for branch_name in branches:
            if not(utils.check_branch_exists(src_repo_url, prefix + branch_name)) and len(prefix + branch_name) > 0:
                new_branches.append(prefix +branch_name)
        return new_branches

    def push_branch(self, local_repo, branch_name, base_branch):
        """This function creates and pushes a new branch from the local repository to the remote repository.

        Args:
            local_repo (str): The local repository to push the branch from.
            branch_name (str): The name of the branch to create and push.
        """
        
        subprocess.run(['git', '-C', local_repo,'checkout', '-b', branch_name, base_branch], shell=False)
        
        subprocess.run(['git', '-C', local_repo, 'push', '-u', 'origin', branch_name], shell=False)
        # subprocess.run(['git', '-C', local_repo, 'push', '--set-upstream', 'origin', branch_name], shell=False)
        pass

    def src_pool_checkout(self, branch_name):
        subprocess.run(['git', '-C', self._src_pool_path, 'checkout', branch_name], shell=False)
        pass
        
    def dst_pool_checkout(self, branch_name):
        subprocess.run(['git', '-C', self._dst_pool_path, 'checkout', branch_name], shell=False)

        pass

    def pull_new_branch(self, src_repo_url, src_branch_name, dst_branch_name, internal_branch_base):
        
        if not(utils.check_branch_exists(branch_name=src_branch_name, remote_repo_url=src_repo_url)):
            self.push_branch(local_repo=self._src_pool_path, branch_name=src_branch_name, base_branch = internal_branch_base)
            
        #copy content here to current branch.
        subprocess.run(['git', '-C', self._src_pool_path, 'checkout', src_branch_name], shell=False)
        subprocess.run(['git', '-C', self._dst_pool_path, 'checkout', dst_branch_name], shell=False)

        self.exclude_dst_repo_info()
        utils.copy_dir(self._dst_pool_path, self._src_pool_path)
        self.include_dst_repo_info()
        # subprocess.run(['git', '-C', self._src_pool_path, 'push', '-u', 'origin', src_branch_name], shell=False)

        self.push_to_src()
        pass

    def pull_all_new_branches(self, src_repo_url, prefix, fetch_base): 
        new_branches = self.git_new_branches(src_repo_url, prefix) # add prefix.
        for new_branch in new_branches:
            self.push_branch(self._src_pool_path, new_branch, fetch_base)
            #copy content here to current branch.
            subprocess.run(['git', '-C', self._dst_pool_path, 'checkout', new_branch], shell=False)
            self.exclude_dst_repo_info()
            utils.copy_dir(self._dst_pool_path, self._src_pool_path)
            self.include_dst_repo_info()
            self.push_to_src()
        pass
    
    def clean_pool(self): 
        """
        This function cleans the temporary files and directories of the pool.
        """

        print('Cleaning pool...')
        utils.rm_dir(self._pool_path)
        pass


