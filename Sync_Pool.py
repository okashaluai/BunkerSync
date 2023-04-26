from Sync_Filter import Sync_Filter
import os
import subprocess

class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        pass
    
    def filter_pool(self, branch, filter : Sync_Filter):
        #switch to branch
        filter.apply_filter(self._pool_path) # todo
        pass
    def init_pool(self):
        pass
    def clone_from_source(self, source_repo_url):
        os.chdir(self._pool_path)
        subprocess.run(['git', 'clone', source_repo_url], shell=True)
        output = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
        print(output)

    def merge_to_target(self, target_repo_url):
        pass
    pass