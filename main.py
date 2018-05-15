from flask import Flask
from pyodbc import *
from core.routes import routes
from importlib import import_module
from core.io import err
from core import config
from flask.helpers import url_for
from flask import send_from_directory
import os
import traceback

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'small aim is crime'
    
    for route in routes:
        __import__(route['package'])
        app.register_blueprint(import_module('.views', route['package']).__dict__[route['package']], url_prefix='/' + route['uri'])
    
    
    return app

app = create_app()

@app.route('/static/<path:filename>')
def serve_static(filename = 'index.html'):
    root_dir = os.getcwd() #os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)


@app.errorhandler(500)
def error_500(error):
    if config.ENV_PRODUCTION:
        return err(msg="some error occurred", status = 500), 500
    else:
        trace = traceback.format_exc()
        app.logger.error(error)
        app.logger.error(trace)
        return err(trace, msg="Error: " + str(error), status = 500), 500
    
@app.errorhandler(404)
@app.errorhandler(405)
def error_404(error):
    print("asdfdfa")
    if config.ENV_PRODUCTION:
        return err(msg="service not found (ensure there is no trailing slash in your URL and the request method GET, POST etc)", status = 404), 404
    else:
        app.logger.error(error)
        return err(str(error), msg="service not found (ensure there is no trailing slash in your URL and the request method GET, POST etc)", status = 404), 404

@app.errorhandler(Exception)
def unhandled_exception(error):
    if config.ENV_PRODUCTION:
        return err(msg="some error occurred", status = 500), 500
    else:
        trace = traceback.format_exc()
        app.logger.error(error)
        app.logger.error(trace)
        return err(trace, msg="Error : " + str(error), status = 500), 500

print(__name__)
if __name__ == '__main__':
    app.run(config.HOST, config.PORT, False)
