from .file_manager_interface import FileManagerInterface
import json
import os


class JsonFileManager(FileManagerInterface):   

    def __init__(self) -> None:
        self.filepath = os.path.join('movie_web_app', 'data', 'movie_database.json')

    def read_file(self):
        with open(self.filepath) as fileobj:
            json_file_content = json.load(fileobj)
        return json_file_content

    def write_to_file(self, data):
        with open(self.filepath, 'w') as fileobj:
            json.dump(data, fileobj, indent=4)
