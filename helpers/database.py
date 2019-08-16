import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))

config_name = os.getenv('APP_SETTINGS')
database_uri = os.getenv('DEV_DATABASE_URL')
engine = create_engine(database_uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()