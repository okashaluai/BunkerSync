from abc import ABC, abstractmethod

class Sync_Filter(ABC):
    def __init__(self, filter_name):
        self._filter_name = filter_name
        pass

    @abstractmethod
    def apply_filter(self, path_to_filter):
        pass
    pass