__author__ = "Sanjeev Kumar"
__email__ = "sanjeev.k@srijan.net"
__copyright__ = "Copyright 2019, Srijan Technologies"


import os
import time
import json
from settings import config, app
from thirdparty import cel
from flask_cors import CORS
from routes import register_urls
from flask_restful import Api

app.url_map.strict_slashes = False

# Swagger configuration
SWAGGER_CONFIG = config.get('SWAGGER_CONFIG')

api = Api(app,)

cel.autodiscover_tasks (["services.background.jobs"])

# CORS whitelisting.
CORS(app, origins=config['CORS_ORIGIN_REGEX_WHITELIST'])

# Registering routes.
register_urls(api)


@app.route("/")
@app.route("/api")
def index():
    return json.dumps({"message": "Welcome to twitter sentimental analysis backend service!! TEST-API"})


if __name__ == '__main__':
    os.environ['APP_CONFIG'] = 'config.LocalConfig'
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)
