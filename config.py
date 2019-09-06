# config file borrowed from Django
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    '''
        Base Config Class. Properties defined below.
    '''
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '4j5rrt85tkdf4'


class ProductionConfig(Config):
    '''
        Production environment config variables
    '''
    DEBUG = False


class StagingConfig(Config):
    '''
        Staging environment config variables
    '''
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    '''
        Development environment config variables
    '''
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    '''
        Testing environment config variables
    '''
    TESTING = True
