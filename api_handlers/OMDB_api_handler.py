import requests
from requests.models import Response


class OMDBApiHandler:

    def __init__(self):
        self.api_key: str = 'http://www.omdbapi.com/?apikey=66544728&t='

    def return_api_response(self, movie_title: str) -> Response:
        """
        return an api response based on a query parameter
        :api_param movie_name:
        :return:
        """
        api_response = requests.get(self.api_key + movie_title)
        return api_response

    def convert_json_api_dict_to_python_dict(self, api_response) -> dict:
        python_object = api_response.json()
        return python_object

