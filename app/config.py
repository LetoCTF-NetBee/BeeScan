class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = None
    ENV = 'production'


class ProductionConfig(Config):
    SECRET_KEY = 'super-secret'
    ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev-key'
    ENV = 'development'
