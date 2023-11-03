from abc import ABC, abstractmethod

class FileManagerInterface(ABC):

    @abstractmethod
    def read_file(self, filename):
        pass

    @abstractmethod
    def write_to_file(self, filename, data):
        pass
