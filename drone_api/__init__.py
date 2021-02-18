from flask import Flask
from flask_cors import CORS

# TODO: Import Config Object for Flask Project
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# Import for Flask Login
from flask_login import LoginManager

# import for authlib integrations
from authlib.integrations.flask_client import OAuth

# import for flask-marshmallow
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'signin' #Specify what page to load for NON-AUTHED users

oauth = OAuth(app)

ma = Marshmallow(app)

from drone_api import routes, models