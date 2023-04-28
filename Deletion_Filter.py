from Sync_Filter import Sync_Filter
import os
import shutil
class deletion_filter(Sync_Filter):
    def __init__(self):
        super().__init__("Deletion filter")
    
    def apply_filter(self, path_to_filter):
        print(self._filter_name + ":")
        with open("./sync_config/roadside.txt", "r") as roadside:
            targets = roadside.readlines()
            for target in targets:
                full_path = path_to_filter/(target.replace('\n', ''))
                if os.path.exists(full_path):
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                        print(full_path, "was deleted!")
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path, ignore_errors=False, onerror=None)
                        print(full_path , "was deleted!")
                else:
                    print(full_path , "does not exist.")
