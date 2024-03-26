from db_configuration import Session
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
import os

# Load environment variables from .env file
load_dotenv()  
# instantiate an instance of the flask app
app = Flask(__name__)
# setsecret key for the app instance, used to encrypt session data
app.secret_key = os.environ.get('SECRET_KEY')
# enable CORS for the app instance
CORS(app)

@app.teardown_appcontext
def remove_session(exception=None):
    Session.remove()