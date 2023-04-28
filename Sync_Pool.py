from Sync_Filter import Sync_Filter
import os
import subprocess
import pathlib
import numpy
import shutil

class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        pass
    
    def filter_pool(self, filter : Sync_Filter):
        filter.apply_filter(self._pool_path) # todo
        pass


    def clone_from_source(self, branch, source_repo_url):
        subprocess.run(['git', 'clone', '--branch', branch, source_repo_url, self._pool_path], shell=True)

        #subprocess.run(['git', 'clone', source_repo_url, ], shell=True)
        #switch to requested branch
        subprocess.run(['git', '-C', self._pool_path,  'checkout', '--orphan', branch], shell=True)

    def merge_to_target(self, target_repo_url, branch):
        default_branch = branch
        
        random_id = str(int(numpy.random.rand(1, 1)[0][0] * 1000000000000))

        temp_branch_name = default_branch + 'temp_branch' + '_'+ random_id
        # subprocess.run(['git', '-C', self._pool_path,  'checkout', branch], shell=True)



        subprocess.run(['git', '-C', self._pool_path, 'remote', 'add', 'target', target_repo_url], shell=True)
        # subprocess.run(['git', '-C', self._pool_path, 'pull', 'target', branch, '--allow-unrelated-histories' ], shell=True)
        # subprocess.run(['git', 'fetch'], shell=True)
        # subprocess.run(['git', 'rebase',branch], shell=True)
        # print('here')
        subprocess.run(['git', '-C', self._pool_path, 'push', 'target', branch], shell=True)


        pass


    def clean_pool(self): #to complete
        if os.path.exists(self._pool_path):
            print('Cleaning pool...')
            shutil.rmtree(self._pool_path, ignore_errors=True)
            # subprocess.run(['rm', '-rf', self._pool_path], shell=True)
    pass