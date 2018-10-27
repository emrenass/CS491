from Backend_API.database import database_config

class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    BABEL_DEFAULT_LOCALE = "en"
    SEND_FILE_MAX_AGE_DEFAULT = 0


class FlaskProductionConfig(FlaskConfig):

    SECRET_KEY = "7d441f27d441f27567d441f2b6176a"

    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_PROTECTION = 'strong'
    SESSION_COOKIE_HTTPONLY = True


    LANGUAGES = {
        'en': 'English'
    }

    DB_HOST = database_config.DB_HOST
    DB_PORT = database_config.DB_PORT
    DB_NAME = database_config.DB_NAME
    DB_USERNAME = database_config.DB_USERNAME
    DB_PASS = database_config.DB_PASS

    HOST = '0.0.0.0'
    PORT = '5090'

    SSL_CERT = 'certificates/test.com.crt'
    SSL_KEY = 'certificates/test.com.key'

    SECURE = True
    HTTPONLY = True


class FlaskDevelopmentConfig(FlaskConfig):
    DEBUG = True
    TESTING = True

    SECRET_KEY = "7d441f27d441f27567d441f2b6176a"

    DB_HOST = database_config.DB_HOST
    DB_PORT = database_config.DB_PORT
    DB_NAME = database_config.DB_NAME
    DB_USERNAME = database_config.DB_USERNAME
    DB_PASS = database_config.DB_PASS

    HOST = 'localhost'
    PORT = '5090'

    SSL_CERT = 'certificates/test.com.crt'
    SSL_KEY = 'certificates/test.com.key'

    SECURE = False
    HTTPONLY = False



