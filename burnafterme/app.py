from flask import Flask

def create_app(profile='ProdProfile'):
    app = Flask(__name__)
    app.config.from_object(f'burnafterme.config.{profile}')

    from burnafterme.routes import service

    app.register_blueprint(service)
    return app

