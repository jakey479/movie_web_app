from abc import ABC, abstractmethod

class FileManagerInterface(ABC):

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_to_file(self, data):
        pass