import requests
from requests.models import Response


class OMDBApiHandler:

    def __init__(self):
        self.api_key: str = 'http://www.omdbapi.com/?apikey=66544728&t='

    def return_api_response(self, movie_title: str) -> Response:
        """
        return an api response from the OMDB api based on a title query parameter
        :movie_title: the name of a movie existing in the api
        :return: an api response if the movie exists in the api
        """
        api_response = requests.get(self.api_key + movie_title)
        return api_response

    def is_api_response_valid(self, api_response: Response) -> bool:
        if self.convert_api_response_to_python_dict(
            api_response=api_response
            )["Response"] == "False": 
            return False
        return True

    def convert_api_response_to_python_dict(self, api_response: Response) -> dict:
        movie_dictionary = api_response.json()
        return movie_dictionary
    
    def return_formatted_movie_dictionary(self, movie_dictionary: dict) -> dict:
        movie_dictionary = {
            "title": movie_dictionary['Title'],
            "release date": movie_dictionary["Released"],
            "director": movie_dictionary["Director"]
        }
        return movie_dictionary
    
    def return_formatted_api_response(self, api_response: Response) -> dict:
        api_response_converted_to_dict = self.convert_api_response_to_python_dict(
            api_response=api_response
        )
        formatted_movie_dictionary = self.return_formatted_movie_dictionary(
            movie_dictionary=api_response_converted_to_dict
        )
        return formatted_movie_dictionary

