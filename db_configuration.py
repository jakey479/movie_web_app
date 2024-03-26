import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# setting the path to the database and passing to the engine object
base_directory = os.path.abspath(os.path.dirname(__file__))
database_name = os.environ.get('DATABASE_NAME')
db_path = os.path.join(base_directory, 'data', database_name)

# create engine object that will connect to the database and handle sql transactions
engine = create_engine('sqlite:///' + db_path)

# create sessions objects where transactions are staged before being comitted via the engine
session_factory = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

# ensure sessions are handled within their own independent threads, preventing concurrency issues
Session = scoped_session(session_factory)