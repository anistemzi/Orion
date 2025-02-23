from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *
from models import Game

if __name__ == '__main__':
    app.run(debug=True)
