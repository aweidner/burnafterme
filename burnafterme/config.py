
class DevProfile:
    DEBUG = True
    REDIS_URL = 'localhost:6379'
    HOST = 'localhost'
    PROTOCOL = 'http'


class ProdProfile:
    DEBUG = False
    REDIS_URL = 'localhost:6379'
    HOST = 'burnafter.me'
    PROTOCOL = 'https'
