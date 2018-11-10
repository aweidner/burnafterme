
class DevProfile:
    DEBUG = True
    REDIS_URL = 'localhost:6379'
    HOST = 'localhost'
    PROTOCOL = 'http'
    TIMEOUT = 10

class ProdProfile:
    DEBUG = False
    REDIS_URL = 'localhost:6379'
    HOST = 'burnafter.me'
    PROTOCOL = 'https'
    TIMEOUT = 60 * 60 * 24 * 7
