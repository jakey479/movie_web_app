from .class_interfaces import FileManagerInterface
import json
import os


class JsonFileManager(FileManagerInterface):        

    def read_file(self, filepath):
        with open(filepath) as fileobj:
            json_file = json.load(fileobj)
        return json_file

    def write_to_file(self, filepath: str, data):
        with open(filepath, 'w') as fileobj:
            json.dump(data, fileobj, indent=4)


