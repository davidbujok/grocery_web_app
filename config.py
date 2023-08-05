import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nice-commands-come-short'
    SQLALCHEMY_DATABASE_URI = "postgresql://davidbujok@localhost:5432/bread_butter" 
    SQLALCHEMY_ECHO = True

