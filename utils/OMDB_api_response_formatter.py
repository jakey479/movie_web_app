class OMDBApiResponseFormatter():

    def return_formatted_movie_dictionary(self, movie_dictionary: dict):
        movie_dictionary = {
            "title": movie_dictionary['Title'],
            "release date": movie_dictionary["Released"],
            "director": movie_dictionary["Director"]
        }
        return movie_dictionary