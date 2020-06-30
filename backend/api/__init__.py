from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from api.config import BaseConfig

app = Flask(__name__)

CORS(app)

config = BaseConfig()
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api.models import *
from api.routes import *
