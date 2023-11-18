from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from uuid import uuid4
from data_management.file_manager_classes import JsonFileManager
from data_management.crud_user_data_classes import JsonCrudUserData
from utils.OMDB_api_handler import OMDBApiHandler
from utils.login_manager_class import LoginManager

app = Flask(__name__)
app.secret_key = str(uuid4())
CORS(app)
file_manager = JsonFileManager()
omdb_api_handler = OMDBApiHandler()
login_manager = LoginManager(
    user_database=file_manager.read_file()
)
crud_user_data = JsonCrudUserData(
    filemanager=file_manager
)


@app.route('/', methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        if 'username' in session:
            del session['username']
        return render_template('user_login.html')
    if request.method == "POST":
        password_attempt = request.form['password']
        username_attempt = request.form['username']
        is_valid_login = login_manager.is_valid_login(
            username_attempt=username_attempt,
            password_attempt=password_attempt
        )
        if is_valid_login:
            session['username'] = username_attempt
            return redirect(url_for('display_user_movies'))
        return render_template('user_login.html')
    
@app.route('/add_user', methods=["POST"])
def add_user():
    username = request.form['username']
    password = request.form['password']
    crud_user_data.add_user(
        username=username,
        password=password
        )
    return redirect(url_for('movie_database_users'))
    
@app.route('/display_user_movies')
def display_user_movies():
    return render_template(
        'user_movies_data.html', 
        user_movies=crud_user_data.return_user_movies(username=session.get('username')),
        username=session.get('username'))

@app.route('/users/add_movie/', methods=['POST'])
def add_movie_to_user_database():
    title = request.form['title']
    api_response = omdb_api_handler.return_api_response(movie_title=title)
    if omdb_api_handler.is_api_response_valid(api_response=api_response):
        formatted_movie_dictionary = omdb_api_handler.return_formatted_api_response(
            api_response=api_response
        )
        crud_user_data.add_movie(
            username=session.get('username'),
            movie_data=formatted_movie_dictionary
            )
        return redirect(url_for('display_user_movies'))
    
@app.route('/users/update_movie/<movie_id>', methods=["POST"])
def update_movie(movie_id):
    crud_user_data.update_user_movie(
        username=session.get('username'),
        movie_id=movie_id,
        movie_dictionary={
            "title": request.form['title'],
            "release date": request.form["release date"],
            "director": request.form["director"]
            }
    )
    return redirect(url_for('display_user_movies'))

@app.route('/users/delete_movie/<movie_id>')
def delete_user_movie(movie_id):
    crud_user_data.delete_user_movie(
        username=session.get('username'), 
        movie_id=movie_id
        )
    return redirect(url_for('display_user_movies'))

if __name__ == '__main__':
    app.run(debug=True, port ='5000')