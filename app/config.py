class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = None
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SECRET_KEY = 'super-secret'
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'  # TODO: some SQL server in docker


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev-key'
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    TEMPLATES_AUTO_RELOAD = True
