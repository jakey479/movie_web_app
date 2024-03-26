from app_configuration import app
from db_configuration import Session
from data_management.data_manager_classes import SqliteDataManager
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS
import os
from utils.OMDB_api_handler import OMDBApiHandler
from utils.login_manager_class import SqliteLoginManager
from werkzeug.security import generate_password_hash

data_manager = SqliteDataManager()
omdb_api_handler = OMDBApiHandler()
login_manager = SqliteLoginManager(
    data_manager=data_manager
)



@app.route('/', methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template('user_login.html')
    if request.method == "POST":
        email_attempt = request.form['email']
        password_attempt = request.form['password']
        if login_manager.is_valid_login(
            email_attempt=email_attempt,
            password_attempt=password_attempt
        ):
            session['email'] = email_attempt
            session['user_id'] = data_manager.return_user_id(email=email_attempt)
            return redirect(url_for('display_user_movies'))
        return redirect(url_for('user_login'))
    
@app.route('/add_user', methods=["POST"])
def add_user():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password=password)
    data_manager.add_user(
        name=name,
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    # if username in data_manager.users_database:
    #     flash('Username already taken') 
    #     return render_template('user_login.html')
    return redirect(url_for('user_login'))
    
@app.route('/display_user_movies')
def display_user_movies():
    return render_template(
        'user_movies_data.html', 
        user_movies=data_manager.return_user_movies(email=session.get('email')),
        username=session.get('username'))

@app.route('/users/add_movie/', methods=['POST'])
def add_movie_to_user_database():
    title = request.form['title']
    api_response = omdb_api_handler.return_api_response(movie_title=title)
    if omdb_api_handler.is_api_response_valid(api_response=api_response):
        formatted_movie_dictionary = omdb_api_handler.return_formatted_api_response(
            api_response=api_response
        )
        data_manager.add_movie(
            username=session.get('username'),
            movie_data=formatted_movie_dictionary
            )
        return redirect(url_for('display_user_movies'))
    else:
        return render_template('movie_not_available.html')
    
@app.route('/users/update_movie/<movie_id>', methods=["POST"])
def update_movie(movie_id):
    data_manager.update_user_movie(
        username=session.get('username'),
        movie_id=movie_id,
        movie_dictionary={
            "title": request.form['title'],
            "director": request.form["director"],
            "cast": request.form["cast"],
            "release date": request.form["release date"],
            "plot": request.form["plot"]
            }
    )
    return redirect(url_for('display_user_movies'))

# @app.route('/users/delete_movie/<movie_id>')
# def delete_user_movie(movie_id):
#     data_manager.delete_user_movie(
#         username=session.get('username'), 
#         movie_id=movie_id
#         )
#     return redirect(url_for('display_user_movies'))

if __name__ == '__main__':
    app.run(debug=True, port ='5000')