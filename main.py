from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from data_management.crud_classes import MovieDatabaseCrud
from data_management.file_manager_classes import JsonFileManager
from api_handlers.OMDB_api_handler import OMDBApiHandler
from api_handlers.OMDB_api_response_formatter import OMDBApiFormatter
import os

app = Flask(__name__)
CORS(app)
json_file_manager = JsonFileManager()
filepath = os.path.join('data', 'movie_database.json')
crud_movie_database_json = MovieDatabaseCrud(filepath=filepath, filemanager=json_file_manager)
omdbp_api_handler = OMDBApiHandler()
omdbp_api_response_formatter = OMDBApiFormatter()
MOVIE_DATABASE = crud_movie_database_json.return_movie_database()



@app.route('/return_users')
def movie_database_users():
    user_names = crud_movie_database_json.return_users(movie_database=MOVIE_DATABASE)
    return render_template('movie_database_users.html', user_names = user_names)

@app.route('/users/<user_id>', methods=['GET'])
def user_movie_data(user_id):
        user_movies = crud_movie_database_json.return_user_movies(
        movie_database=MOVIE_DATABASE,
        user_id=user_id
        )
        return render_template('user_movies_data.html', user_movies=user_movies, user_id=user_id)

@app.route('/add_user')
def add_user_to_database():
    # displays a form to add a user

@app.route('/users/add_movie/<user_id>', methods=['GET', 'POST'])
def add_movie_to_user_database(user_id):
    title = request.form['title']
    release_date = request.form['release_date']
    director = request.form['director']
    user_id = user_id
    api_response = omdbp_api_handler.return_api_response(movie_title=title)
    movie_dictionary = omdbp_api_response_formatter.return_formatted_movie_dictionary(
         json_response=omdbp_api_handler.convert_api_json_response_to_python_object(
              api_response=api_response
              )
    )
    crud_movie_database_json.add_movie_dictionary(
        user_id=user_id,
        movie_database=MOVIE_DATABASE,
        movie_dictionary=movie_dictionary
        )
    return redirect(url_for('user_movie_data', user_id=user_id))



# @app.route('/users/<user_id>/update_movie/<movie_id>')
# def update_movie(user_id, movie_id):
#     MovieDatabaseCrud.update_user_movie(
#         user_id=user_id,
#         movie_database=movie_database,
#         movie_id=movie_id,
#         movie_key = None,
#         movie_value= None
#     )

# @app.route('/users/<user_id>/delete_movie/<movie_id>')
# def delete_user_movie(user_id, movie_id):
#     MovieDatabaseCrud.delete_movie_dictionary(
#         user_id=user_id,
#         movie_database=movie_database,
#         movie_id=movie_id
#         )

if __name__ == '__main__':
    app.run(debug=True, port ='5000')