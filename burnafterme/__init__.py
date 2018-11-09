from burnafterme.app import create_app
from flask_redis import FlaskRedis

app = create_app()
redis_client = FlaskRedis(app)

