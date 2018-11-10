from flask import Blueprint, request, current_app
from burnafterme.lib import generate_short, parse_timeout, TimeoutFormatException

service = Blueprint('service', __name__)

@service.route('/', methods=['PUT'])
def add_data():
    from burnafterme import redis_client

    if not request.data:
        return '400 NO CONTENT', 400 

    key = generate_short()

    timeout = current_app.config['TIMEOUT']
    user_provided_timeout = request.args.get('t')
    print(user_provided_timeout)
    if user_provided_timeout:
        try:
            timeout = parse_timeout(user_provided_timeout)
        except TimeoutFormatException:
            return f'400 BAD TIMEOUT PROVIDED {request.args.get("t")}'
        except Exception:
            return f'400 LOGICAL TIMEOUT EXCEPTION'

    redis_client.setex(key, timeout, request.data)
    return f'{current_app.config["PROTOCOL"]}://{current_app.config["HOST"]}/{key}'


@service.route('/<key>', methods=['GET'])
def get_data(key):
    from burnafterme import redis_client

    result = redis_client.get(key)
    if result is None:
        return '404 NOT FOUND', 404
    try:
        return result
    finally:
        redis_client.delete(key)
