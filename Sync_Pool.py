from Sync_Filter import Sync_Filter
import os
import subprocess
import pathlib
import numpy
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
            #clone branch of repositories src,dst -> pool
            subprocess.run(['git', 'clone', '--branch', branch_name, dst_repo_url, self._dst_pool_path], shell=True)
            subprocess.run(['git', 'clone', '--branch', branch_name, src_repo_url, self._src_pool_path], shell=True)

            # copy subdirectory src -> dst
            from_directory = str(self._src_pool_path)
            to_directory = str(self._dst_pool_path)
            rm_dir(self._src_pool_path/'.git')
            copy_tree(from_directory, to_directory)

            #subprocess.run(['git', '-C', self._dst_pool_path, 'remote', 'set-url', 'origin', dst_repo_url], shell=True)
            
        else:
            pass
        pass

    def merge_to_dst(self, src_repo_url):
        subprocess.run(['git', '-C',self._dst_pool_path, 'add', '.'], shell=True)
        subprocess.run(['git', '-C', self._dst_pool_path, 'commit', '-m', 'Merge from: ' + src_repo_url ], shell=True)
        subprocess.run(['git', '-C',self._dst_pool_path, 'push' , 'origin'], shell=True)
        pass

    
    def clone_from_source(self, branch, source_repo_url):
        subprocess.run(['git', 'clone', '--branch', branch, source_repo_url, self._pool_path], shell=True)
        subprocess.run(['git', '-C', self._pool_path,  'checkout', '--orphan', branch], shell=True)
    def merge_to_target(self, target_repo_url, branch):
        
        random_id = str(int(numpy.random.rand(1, 1)[0][0] * 1000000000000))

        temp_branch_name = 'temp_branch' + '_'+ random_id

        # git clone dst 
        # checkout -b temp 
        # \cp -r src dst 
        # filtering the temp
        # git add commit push 
        # firefox dst url
        

        subprocess.run(['git', '-C', self._pool_path, 'remote', 'add', 'target', target_repo_url], shell=True)
        # subprocess.run(['git', '-C', self._pool_path, 'pull', 'target', branch, '--allow-unrelated-histories' ], shell=True)
        # subprocess.run(['git', 'fetch'], shell=True)
        # subprocess.run(['git', 'rebase',branch], shell=True)
        # print('here')
        subprocess.run(['git', '-C', self._pool_path, 'push', 'target', branch + ':'+ temp_branch_name], shell=True)


        pass


    def clean_pool(self): 
        print('Cleaning pool...')
        rm_dir(self._pool_path)
        pass


