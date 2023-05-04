from abc import ABC, abstractmethod

class Sync_Filter(ABC):
    def __init__(self, filter_name):
        self._filter_name = filter_name
        pass

    @abstractmethod
    def apply_filter(self, path_to_filter):
        """
        Abstract method that enables implementing it as a filter application given a directory to filter.

        Args:
            path_to_filter (Path): path of directory to filter its content.
        """
        pass
    pass