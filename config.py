import os

from envparse import env

ENV = env.str('ENV', default='.env')
if os.path.isfile(ENV):
    env.read_envfile(ENV)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = env.bool('DEBUG', default=False)

FLASK_RUN_HOST = env.str('APP_HOST', default='127.0.0.1')
FLASK_RUN_PORT = env.str('APP_PORT', default='8000')
SECRET_TOKEN = env.str('SECRET_TOKEN', default='secret_token_1')


class Config:
    # default config settings
    DEBUG = False
    TESTING = False
    SECRET_KEY = env.str('SECRET_KEY', default='')


class ProductionConfig(Config):
    # config settings for production
    pass


class DevelopmentConfig(Config):
    # config settings for development
    DEBUG = True
    SECRET_KEY = 'dev'


class TestingConfig(Config):
    TESTING = True