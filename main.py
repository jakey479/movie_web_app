from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from uuid import uuid4
from utils import helpers
from data_management.crud_classes import MovieDatabaseCrud
from data_management.file_manager_classes import JsonFileManager
from api_handlers.OMDB_api_handler import OMDBApiHandler
from api_handlers.OMDB_api_response_formatter import OMDBApiFormatter
import os

app = Flask(__name__)
app.secret_key = str(uuid4())
CORS(app)
json_file_manager = JsonFileManager()
filepath = os.path.join('data', 'movie_database.json')
crud_movie_database_json = MovieDatabaseCrud(filepath=filepath, filemanager=json_file_manager)
omdbp_api_handler = OMDBApiHandler()
omdbp_api_response_formatter = OMDBApiFormatter()

# this is the first route that users will be directed to aka the homepage. Username and user_id's are passed to the route so that the route can dynamically generate elements with usernames that corresponds to the appropriate user_id
@app.route('/return_users')
def movie_database_users():
    user_names = crud_movie_database_json.return_users()
    return render_template('movie_database_users.html', user_names=user_names)

# this route is only ever accessed from a post request because the only link to this route occurs via a form. This link is only refereced via the movie_database_users.html template
@app.route('/add_user', methods=["POST"])
def add_user_to_database():
    user_name = request.form['username']
    user_password = request.form['password']
    hashed_user_password = helpers.return_hashed_password(password=user_password)
    crud_movie_database_json.add_new_user(
        username=user_name,
        user_password=hashed_user_password
        )
    return redirect(url_for('movie_database_users'))

# this route returns a login page which will redirect to the user_movies_data.html page if the login is correct and will redirect to the movie_database_users.html page if login is not correct
@app.route('/user_login/<user_id>', methods=["GET", "POST"])
def user_login(user_id):
        if request.method == 'GET':
            session['user_id'] = user_id
            return render_template('user_login.html', user_id=user_id)
        if request.method == 'POST':
            username_attempt = request.form['username']
            password_attempt = request.form['password']
            username = crud_movie_database_json.return_username(user_id=user_id)
            password = crud_movie_database_json.return_user_password(user_id=user_id)
            print(username, username_attempt)
            print(password, password_attempt)
            if helpers.is_valid_password(
                hashed_password=password, 
                password_attempt=password_attempt
                ) and username_attempt == username:
                return redirect(url_for('user_movie_data'))
            return redirect(url_for('movie_database_users'))
     
# this is the route that users will be directed to if they select a user_name from the movie_database_users.html user list. Returns a users data, storing the user_id as the
@app.route('/users', methods=["GET", 'POST'])
def user_movie_data():
        # everytime this function/app.route is accessed (when a new user is selected from the main menu),      session['user_id'] should take on the value of the new user_id which is also accessible across routes
        user_movies = crud_movie_database_json.return_user_movies(
        user_id=session.get('user_id')
        )
        return render_template(
            'user_movies_data.html', 
            user_movies=user_movies
            )
    
@app.route('/users/add_movie/', methods=['GET', 'POST'])
def add_movie_to_user_database():
    title = request.form['title']
    api_movie_response = omdbp_api_handler.return_api_response(movie_title=title)
    movie_dictionary = omdbp_api_handler.convert_json_api_dict_to_python_dict(
        api_response=api_movie_response
        )
    formatted_movie_dictionary = omdbp_api_response_formatter.return_formatted_movie_dictionary(
         movie_dictionary=movie_dictionary
    )
    crud_movie_database_json.add_movie_dictionary(
        user_id=session.get('user_id'),
        movie_dictionary=formatted_movie_dictionary
        )
    return redirect(url_for('user_movie_data', user_id=session.get('user_id')))



@app.route('/users/update_movie/<movie_id>', methods=["POST"])
def update_movie(movie_id):
    crud_movie_database_json.update_user_movie(
        user_id=session.get('user_id'),
        movie_id=movie_id,
        movie_dictionary={
            "title": request.form['title'],
            "release date": request.form["release date"],
            "director": request.form["director"]
            }
    )
    return redirect(url_for('user_movie_data', user_id=session.get('user_id')))

@app.route('/users/delete_movie/<movie_id>')
def delete_user_movie(movie_id):
    crud_movie_database_json.delete_movie_dictionary(
        user_id=session.get('user_id'), 
        movie_id=movie_id,
        )
    return redirect(url_for('user_movie_data', user_id=session.get('user_id')))

if __name__ == '__main__':
    app.run(debug=True, port ='5000')