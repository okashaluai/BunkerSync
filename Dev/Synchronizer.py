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
    
    def sync_internal_external(self, src_repo_url, dst_repo_url, branch_name):
        """_summary_

        Args:
            src_repo_url (_type_): _description_
            dst_repo_url (_type_): _description_
            branch_name (_type_): _description_
        """
        self._sync_pool.clone_src_dst(src_repo_url, dst_repo_url, branch_name)
        self._sync_pool.local_merge()
        filter = deletion_filter()
        self._sync_pool.filter_src_pool(filter)
        self._sync_pool.filter_dst_pool(filter)
        self._sync_pool.merge_to_dst(src_repo_url)
        self._sync_pool.clean_pool()
        pass

    def sync_external_internal(self, internal_repo_url, external_repo_url):
        """_summary_

        Args:
            internal_repo_url (_type_): _description_
            external_repo_url (_type_): _description_
        """
        self._sync_pool.clone_src(internal_repo_url)
        self._sync_pool.clone_dst(external_repo_url)
        self._sync_pool.pull_new_branches(internal_repo_url)
        self._sync_pool.clean_pool()
        pass


    def run(self, src_repo_url, dst_repo_url, branch_name):
        """_summary_

        Args:
            src_repo_url (_type_): _description_
            dst_repo_url (_type_): _description_
            branch_name (_type_): _description_
        """
        # self.sync_internal_external(src_repo_url, dst_repo_url, branch_name)
        self.sync_external_internal(src_repo_url, dst_repo_url)
    
    
