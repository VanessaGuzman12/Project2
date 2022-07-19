# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

uri = os.getenv("DATABASE_URL","")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://","postgresql://",1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri or "sqlite:///Mortality_causes.sqlite"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Pet