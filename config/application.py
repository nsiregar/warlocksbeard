''' Configuration File '''
import os

class BaseConfig:
    DEBUG = False
    TESTING = False
    DATABASE_CONFIG = {
        'filename': 'filename.db',
        'create_db': True
    }
    DATABASE_PROVIDER = 'sqlite'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
