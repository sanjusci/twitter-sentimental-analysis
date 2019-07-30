import os
from flask import Flask
from etc.conf.env import ENV_CONFIG

__basedir__ = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
config = None
env = os.environ.get('ENV', 'local')

logged_in_user = {}

# Loading configuration
if env in ENV_CONFIG:
    app.config.from_object(ENV_CONFIG[env])
    config = app.config
    config['APPLICATION_ROOT'] = __basedir__
else:
    print("Invalid env name: {}. Available environments are: {}".format(env, ', '.join(ENV_CONFIG.keys())))

__all__ = ["config", "env", "app"]
