from Sync_Filter import Sync_Filter
import subprocess
from distutils.dir_util import copy_tree
from utils import *
class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        self._dst_pool_path = path/'dst'
        self._src_pool_path = path/'src'        
        self.clean_pool()
        pass
    
    def filter_dst_pool(self, filter : Sync_Filter):
        filter.apply_filter(self._dst_pool_path) 
        pass
    def filter_src_pool(self, filter : Sync_Filter):
        filter.apply_filter(self._src_pool_path) 
        pass
    
    
    def clone_src_dst(self, src_repo_url, dst_repo_url, branch_name):
        if branch_exists(dst_repo_url, branch_name):
            print('Branch: "'+branch_name+'" exists in destination repository.\n')
            #clone branch of repositories src,dst -> pool
            subprocess.run(['git', 'clone', '--branch', branch_name, dst_repo_url, self._dst_pool_path], shell=True)
            subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=True)
            
        else:
            print('Branch: "'+branch_name+'" does not exist in destination repository.\n')

            subprocess.run(['git', 'clone',  dst_repo_url, self._dst_pool_path], shell=True)
            subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=True)
            subprocess.run(['git', '-C', self._dst_pool_path,'checkout', '-b', branch_name], shell=True)
            subprocess.run(['git', '-C', self._dst_pool_path, 'push', '--set-upstream', 'origin', branch_name], shell=True)
    
    def local_merge(self):
        # copy subdirectory src -> dst
        from_directory = str(self._src_pool_path)
        to_directory = str(self._dst_pool_path)
        rm_dir(self._src_pool_path/'.git')
        copy_tree(from_directory, to_directory)

        #subprocess.run(['git', '-C', self._dst_pool_path, 'remote', 'set-url', 'origin', dst_repo_url], shell=True)


    def merge_to_dst(self, src_repo_url):
        subprocess.run(['git', '-C',self._dst_pool_path, 'add', '.'], shell=True)
        subprocess.run(['git', '-C', self._dst_pool_path, 'commit', '-m', 'Merge from: ' + src_repo_url ], shell=True)
        subprocess.run(['git', '-C',self._dst_pool_path, 'push' , 'origin'], shell=True)
        pass



    def clean_pool(self): 
        print('Cleaning pool...')
        rm_dir(self._pool_path)
        pass


