from flask import Flask

def create_app():
    """Create the flask app"""
    app = Flask(__name__)
    
    """Add the map to the index endpoint"""
    from . import map 
    app.register_blueprint(map.bp)
    app.add_url_rule('/', endpoint='index')
    
    """Add the API endpoint"""
    from . import api
    app.register_blueprint(api.a)
    app.add_url_rule('/api', endpoint='api')

    return app
