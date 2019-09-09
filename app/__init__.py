from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    from . import map 
    app.register_blueprint(map.bp)
    app.add_url_rule('/', endpoint='index')

    from . import api
    app.register_blueprint(api.a)
    app.add_url_rule('/api', endpoint='api')

    return app
