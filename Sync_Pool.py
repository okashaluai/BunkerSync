from Sync_Filter import Sync_Filter
import os
import subprocess
import pathlib

class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        pass
    
    def filter_pool(self, branch, filter : Sync_Filter):
        #switch to branch
        # curr_dir = pathlib.Path(os.getcwd())

        # repo_path = list(curr_dir.iterdir())[0] # I know that a repo is clone into one dir.
        # #os.chdir(repo_path)
        # print(repo_path)
        # subprocess.run(['git', '-C', repo_path,  'checkout', branch], shell=True)

        filter.apply_filter(self._pool_path) # todo
        pass
    def init_pool(self):
        pass
    def clone_from_source(self, source_repo_url):
        # os.chdir(self._pool_path)
        subprocess.run(['git', 'clone', source_repo_url, self._pool_path], shell=True)
        
    def merge_to_target(self, target_repo_url):
        pass
    pass