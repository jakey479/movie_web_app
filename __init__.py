from app.data_models import Base
from config import database_path as db_path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

from app import routes, models


