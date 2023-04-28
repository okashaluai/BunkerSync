from Sync_Pool import Sync_Pool
from Deletion_Filter import deletion_filter
import os 
from pathlib import Path
class Synchronizer:
    def __init__(self):
        pool_path = Path('./pool')
        config_path = Path('./sync_config')
        if not os.path.exists(pool_path):
            os.makedirs(pool_path)
        if not os.path.exists(config_path):
            os.mkdir(config_path)
        if not os.path.exists(config_path / 'roadside.txt'):
            open(config_path / 'roadside.txt', "x")
        self._sync_pool = Sync_Pool(pool_path)
        pass

    def run(self, src_repo_url, dst_repo_url, branch_name):
        self._sync_pool.clone_src_dst(src_repo_url, dst_repo_url, branch_name)
        filter = deletion_filter()
        self._sync_pool.filter_dst_pool(filter)
        self._sync_pool.merge_to_dst(src_repo_url)
        self._sync_pool.clean_pool()
        pass

