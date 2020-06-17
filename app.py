from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import BaseConfig

app = Flask(__name__)

config = BaseConfig()
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user import *
from models.recipe import *
from routes import *

if __name__ == "__main__":
  app.run(debug=True)