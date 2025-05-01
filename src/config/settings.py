# settings.py

class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///paywall_breaker.db'
    SECRET_KEY = 'your_secret_key_here'
    API_KEY = 'your_api_key_here'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    TIMEZONE = 'UTC'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user:password@localhost/paywall_breaker'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'