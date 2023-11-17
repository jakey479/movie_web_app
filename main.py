from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from uuid import uuid4
from data_management.file_manager_classes import JsonFileManager
from movie_database_app_class import MovieDatabaseApp
from data_management.crud_user_movie_data_classes import JsonCrudUserMovieData

app = Flask(__name__)
app.secret_key = str(uuid4())
CORS(app)
file_manager = JsonFileManager()
movie_database_app = MovieDatabaseApp(filemanager=file_manager)


@app.route('/', methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template('user_login.html')
    if request.method == "POST":
        password_attempt = request.form['password']
        username_attempt = request.form['username']
        is_valid_login = movie_database_app.is_valid_login(
            username_attempt=username_attempt,
            password_attempt=password_attempt
        )
        if is_valid_login:
            movie_database_app.set_user_movies_data(username=username_attempt)
            user_movies = movie_database_app.user_movies_data
            return render_template(
                'user_movies_data.html', 
                user_movies=user_movies,
                username=username_attempt)
        return render_template('user_login.html')

         

# this route is only ever accessed from a post request because the only link to this route occurs via a form. This link is only refereced via the movie_database_users.html template
# @app.route('/add_user', methods=["POST"])
# def add_user_to_database():
#     user_name_attempt = request.form['username']
#     user_password_attempt = request.form['password']
#     movie_database = json_file_manager.read_file()
#     crud_movie_database_json.add_new_user(
#         username=user_name,
#         user_password=hashed_user_password
#         )
#     return redirect(url_for('movie_database_users'))

     
# this is the route that users will be directed to if they select a user_name from the movie_database_users.html user list. Returns a users data, storing the user_id as the
# @app.route('/users', methods=["GET", 'POST'])
# def user_movie_data():
#         # everytime this function/app.route is accessed (when a new user is selected from the main menu),      session['user_id'] should take on the value of the new user_id which is also accessible across routes
#         user_movies = crud_movie_database_json.return_user_movies(
#         user_id=session.get('user_id')
#         )
#         return render_template(
#             'user_movies_data.html', 
#             user_movies=user_movies
#             )
    
# @app.route('/users/add_movie/', methods=['GET', 'POST'])
# def add_movie_to_user_database():
#     title = request.form['title']
#     api_movie_response = omdbp_api_handler.return_api_response(movie_title=title)
#     movie_dictionary = omdbp_api_handler.convert_json_api_dict_to_python_dict(
#         api_response=api_movie_response
#         )
#     formatted_movie_dictionary = omdbp_api_response_formatter.return_formatted_movie_dictionary(
#          movie_dictionary=movie_dictionary
#     )
#     crud_movie_database_json.add_movie_dictionary(
#         user_id=session.get('user_id'),
#         movie_dictionary=formatted_movie_dictionary
#         )
#     return redirect(url_for('user_movie_data', user_id=session.get('user_id')))



# @app.route('/users/update_movie/<movie_id>', methods=["POST"])
# def update_movie(movie_id):
#     crud_movie_database_json.update_user_movie(
#         user_id=session.get('user_id'),
#         movie_id=movie_id,
#         movie_dictionary={
#             "title": request.form['title'],
#             "release date": request.form["release date"],
#             "director": request.form["director"]
#             }
#     )
#     return redirect(url_for('user_movie_data', user_id=session.get('user_id')))

# @app.route('/users/delete_movie/<movie_id>')
# def delete_user_movie(movie_id):
#     crud_movie_database_json.delete_movie_dictionary(
#         user_id=session.get('user_id'), 
#         movie_id=movie_id,
#         )
#     return redirect(url_for('user_movie_data', user_id=session.get('user_id')))

if __name__ == '__main__':
    app.run(debug=True, port ='5000')