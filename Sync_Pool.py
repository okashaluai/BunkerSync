from Sync_Filter import Sync_Filter

class Sync_Pool:

    def __init__(self, path):
        self._pool_path = path
        pass
    
    def filter_pool(self, filter : Sync_Filter):
        filter.apply_filter() # todo
        pass
    def init_pool(self):
        pass
    def clone_from_source(self, source_repo_url):
        pass
    def merge_to_target(self, target_repo_url):
        pass
    pass