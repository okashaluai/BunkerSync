from Sync_Filter import Sync_Filter
import os
import subprocess
import pathlib
import numpy
import shutil, stat, errno

class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        pass
    
    def filter_pool(self, filter : Sync_Filter):
        filter.apply_filter(self._pool_path) # todo
        pass


    def clone_from_source(self, branch, source_repo_url):
        subprocess.run(['git', 'clone', '--branch', branch, source_repo_url, self._pool_path], shell=True)
        subprocess.run(['git', '-C', self._pool_path,  'checkout', '--orphan', branch], shell=True)
    def merge_to_target(self, target_repo_url, branch):
        
        random_id = str(int(numpy.random.rand(1, 1)[0][0] * 1000000000000))

        temp_branch_name = 'temp_branch' + '_'+ random_id



        subprocess.run(['git', '-C', self._pool_path, 'remote', 'add', 'target', target_repo_url], shell=True)
        # subprocess.run(['git', '-C', self._pool_path, 'pull', 'target', branch, '--allow-unrelated-histories' ], shell=True)
        # subprocess.run(['git', 'fetch'], shell=True)
        # subprocess.run(['git', 'rebase',branch], shell=True)
        # print('here')
        subprocess.run(['git', '-C', self._pool_path, 'push', 'target', branch + ':'+ temp_branch_name], shell=True)


        pass


    def clean_pool(self): 
        def onerror(func, path, exc_info):
            """
            Error handler for ``shutil.rmtree``.

            If the error is due to an access error (read only file)
            it attempts to add write permission and then retries.

            If the error is for another reason it re-raises the error.
            
            Usage : ``shutil.rmtree(path, onerror=onerror)``
            """
            import stat
            # Is the error an access error?
            if not os.access(path, os.W_OK):
                os.chmod(path, stat.S_IWUSR)
                func(path)
            else:
                raise

        if os.path.exists(self._pool_path):
            print('Cleaning pool...')
            shutil.rmtree(self._pool_path, ignore_errors=False, onerror=onerror )
        pass