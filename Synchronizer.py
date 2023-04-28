from Sync_Pool import Sync_Pool
from Deletion_Filter import deletion_filter
import os 
from pathlib import Path
class Synchronizer:
    def __init__(self):
        pool_path = Path('./pool')
        config_path = Path('./config')
        if not os.path.exists(pool_path):
            os.mkdir(pool_path)
        if not os.path.exists(config_path):
            os.mkdir(config_path)
        if not os.path.exists(config_path / 'roadside.txt'):
            open(config_path / 'roadside.txt', "x")
        self._sync_pool = Sync_Pool(pool_path)
        pass

    def run(self, source_repo_url, target_repo_url, branch):
        self._sync_pool.clone_from_source(branch, source_repo_url)
        filter = deletion_filter()
        self._sync_pool.filter_pool(filter)
        self._sync_pool.merge_to_target(target_repo_url, branch)
        self._sync_pool.clean_pool()
        pass

