import os

class Config:
    API_KEY = os.getenv('NUMLOOKUP_API_KEY', 'num_live_wUktAqcbd7KHQB3zoaUnTjUxl8ibyxNhT2VdNwXy')
    API_URL = "https://api.numlookupapi.com/v1/validate/"
    DEFAULT_COUNTRY_CODE = "FR"
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
