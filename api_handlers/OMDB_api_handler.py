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

    def convert_api_json_response_to_python_object(self, api_response):
        python_object = api_response.json()
        return python_object

