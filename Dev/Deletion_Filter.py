from Sync_Filter import Sync_Filter
import os
from utils import rm_dir

class deletion_filter(Sync_Filter):
    def __init__(self, filter_map_path):
        super().__init__("Deletion filter")
        self._filter_map_path = filter_map_path
    
    def apply_filter(self, path_to_filter):
        """_summary_

        Args:
            path_to_filter (_type_): _description_
        """
        print(self._filter_name + ":")
        # with open("./sync_config/roadside.txt", "r") as roadside:
        with open(self._filter_map_path, "r") as roadside:
            targets = roadside.readlines()
            for target in targets:
                full_path = path_to_filter/(target.replace('\n', ''))
                if os.path.exists(full_path):
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                        print(full_path, "was deleted!")
                    elif os.path.isdir(full_path):
                        rm_dir(full_path)
                        print(full_path , "was deleted!")
                else:
                    print(full_path , "does not exist.")
