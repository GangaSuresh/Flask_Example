from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#__name__ local python file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db=SQLAlchemy(app)

### this file will be executed first in the package #########

from market import routes