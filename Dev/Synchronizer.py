from Sync_Pool import Sync_Pool
from Deletion_Filter import deletion_filter
import os 
from pathlib import Path
import utils 
class Synchronizer:
    def __init__(self):
        tmp_dir = Path(utils.get_temp_path()) 
        pool_path = Path( tmp_dir / 'pool')
        # config_path = Path(tmp_dir / 'sync_config')
        # if not os.path.exists(config_path):
        #     os.mkdir(config_path)
        # if not os.path.exists(config_path / 'roadside.txt'):
        #     open(config_path / 'roadside.txt', "x")
        self._sync_pool = Sync_Pool(pool_path)
        pass
    
    def sync_internal_external(self, src_repo_url, dst_repo_url, internal_branch_name, external_branch_name, external_branch_base, filter_map_path = None):
        """Synchronizes changes made to a source repository with a destination repository.
           Supports filtering mechanism by passing a filter object to the sync_pool object.

        Args:
            src_repo_url (str): The URL of the source repository.
            dst_repo_url (str): The URL of the destination repository.
            branch_name (str): The name of the branch to synchronize.

        """

        ###################To Customize #################
        if not (filter_map_path is None) and not(os.path.isfile(filter_map_path)): 
            if not(os.path.isfile(self._sync_pool._dst_pool_path / filter_map_path)):
                raise Exception("Filtering map file does not exist neither in the given path nor in the local git repository!")
            else:
                filter_map_path = self._sync_pool._dst_pool_path / filter_map_path
        #################################################

        self._sync_pool.clone_src_dst(
                                    src_repo_url=src_repo_url, 
                                    dst_repo_url=dst_repo_url, 
                                    internal_branch_name=internal_branch_name, 
                                    external_branch_name=external_branch_name, 
                                    external_branch_base= external_branch_base)
        self._sync_pool.local_merge()
        filter = None
        if not (filter_map_path is None):
            filter = deletion_filter(filter_map_path)
        # self._sync_pool.filter_src_pool(filter)
        self._sync_pool.filter_dst_pool(filter)
        self._sync_pool.push_to_dst()
        self._sync_pool.clean_pool()
        pass

    def sync_external_internal_with_prefix(self, internal_repo_url, external_repo_url, prefix, fetch_base):
        """_summary_

        Args:
            internal_repo_url (_type_): _description_
            external_repo_url (_type_): _description_
        """
        
        self._sync_pool.clone_src(internal_repo_url)
        self._sync_pool.clone_dst(external_repo_url)
        self._sync_pool.pull_all_new_branches(internal_repo_url, prefix, fetch_base=fetch_base)
        self._sync_pool.clean_pool()
        pass

    def sync_external_internal_with_branch(self, internal_repo_url, external_repo_url, src_branch_base, dst_branch_name, src_branch_name):
        """_summary_

        Args:
            internal_repo_url (_type_): _description_
            external_repo_url (_type_): _description_
        """
        
        self._sync_pool.clone_src(internal_repo_url)
        self._sync_pool.clone_dst(external_repo_url)
        self._sync_pool.pull_new_branch(
                                src_repo_url = internal_repo_url,  
                                src_branch_name = src_branch_name, 
                                dst_branch_name = dst_branch_name,
                                internal_branch_base = src_branch_base)
        self._sync_pool.clean_pool()
        pass
 
    
    

    def sync(self, src_url, dst_url, src_branch_name, dst_branch_name, base_branch, filter_path):
        if not(utils.check_branch_exists(src_url, src_branch_name)):
            raise Exception('Source repository has no ' + src_branch_name + ' branch!')

        self._sync_pool.clone_src(src_url)
        self._sync_pool.clone_dst(dst_url)
        self._sync_pool.src_pool_checkout(src_branch_name)
        filter = None
        if not (filter_path is None):
            filter = deletion_filter(filter_path)
        # self._sync_pool.filter_src_pool(filter)   : src or dst

        if utils.check_branch_exists(dst_url, dst_branch_name):
            # push temp branch 
            # local merge : self._sync_pool.local_merge()
            # PR temp branch to dst branch 
            pass        

        
        else:
            self._sync_pool.push_branch(self._sync_pool._dst_pool_path, 
                                        dst_branch_name, 
                                        base_branch)
            self._sync_pool.local_merge()
            self._sync_pool.push_to_dst()


        self._sync_pool.clean_pool()
        pass