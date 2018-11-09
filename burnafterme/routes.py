from flask import Blueprint, request, current_app
from burnafterme.lib import generate_short

service = Blueprint('service', __name__)

@service.route('/', methods=['PUT'])
def add_data():
    from burnafterme import redis_client

    if not request.data:
        return "400 NO CONTENT", 400 

    key = generate_short()
    redis_client.set(key, request.data)
    return f'{current_app.config["PROTOCOL"]}://{current_app.config["HOST"]}/{key}'


@service.route('/<key>', methods=['GET'])
def get_data(key):
    from burnafterme import redis_client

    result = redis_client.get(key)
    print(result)
    if result is None:
        return "404 NOT FOUND", 404
    try:
        return result
    finally:
        redis_client.delete(key)
