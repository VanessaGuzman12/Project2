# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Mortality_causes.sqlite"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
class Mortality_causes(db.Model):
    __tablename__ = 'main'
    index = db.Column(db.BIGINT, primary_key =True)
    date_regis = db.Column(db.DATETIME)
    date_ocur = db.Column(db.DATETIME)
    date_nacim = db.Column(db.DATETIME)
    death_cause_desc= db.Column(db.TEXT)
    death_cause_cap = db.Column(db.TEXT)
    state = db.Column(db.TEXT)
    municipality = db.Column(db.TEXT)
    gender = db.Column(db.TEXT)
    scholarity = db.Column(db.TEXT)
    death_age= db.Column(db. FLOAT)





    def __repr__(self):
        return '<Mortality_causes %r>' % (self.name)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["GET", "POST"])
def send():
     results = db.session.query(Mortality_causes.death_age,Mortality_causes.gender).filter(Mortality_causes.municipality)




if __name__ == "__main__":
    app.run()