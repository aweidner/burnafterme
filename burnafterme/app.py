import random
from flask import Flask, request
from flask_redis import FlaskRedis
import redis

app = Flask(__name__)

app.config['REDIS_URL'] = 'localhost:6379'
app.config['HOST'] = 'localhost'
app.config['PROTOCOL'] = 'http' 

redis_client = FlaskRedis(app)

base62chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


def generate_short():
    return ''.join(random.choice(base62chars) for i in range(6))


@app.route('/', methods=['PUT'])
def add_data():
    key = generate_short()
    redis_client.set(key, request.data)
    return f'{app.config["PROTOCOL"]}://{app.config["HOST"]}/{key}'


@app.route('/<key>', methods=['GET'])
def get_data(key):
    result = redis_client.get(key)
    if result is None:
        return "404 NOT FOUND", 404
    try:
        return result
    finally:
        redis_client.delete(key)
