from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy as sa

app = Flask(__name__)
app.config.from_object('config')

# couldn't get this to work with pandas:
#db = SQLAlchemy(app)
#db.init_app(app)

# creating engine here and importing in models does work
engine = sa.create_engine('sqlite:///app/odyssey.db')

# imports really needed even though pycharm doesn't think so:
from app import views, models