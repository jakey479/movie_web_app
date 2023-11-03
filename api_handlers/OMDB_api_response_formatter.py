class OMDBApiFormatter():

    def return_formatted_movie_dictionary(self, json_response: dict):
        movie_dictionary = {
            "title": json_response['Title'],
            "release_date": json_response["Released"],
            "director": json_response["Director"]
        }
        return movie_dictionary