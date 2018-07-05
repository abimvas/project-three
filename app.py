from flask import Flask, render_template, jsonify, json
from models import *
from sqlalchemy.orm import Session
from utils import *
from config import config
import os
import numpy as np
import plotly

#################################################
# Application Config
#################################################

app = Flask(__name__)
config_name = os.getenv("FLASK_ENV", "default")
app.config.from_object(config[config_name])

#################################################
# Database Setup
#################################################

db.init_app(app)

# Populate table if it doesn't exist
with app.app_context():
    if not db.engine.dialect.has_table(db.engine, "temperatures"):
        Temps_Since_1800("db/yearlytempavg1800.csv", app.config["SQLALCHEMY_DATABASE_URI"])


#################################################
# Routes
#################################################

@app.before_first_request
def setup():
    # db.drop_all()
    db.create_all()

@app.route("/")
def index():

    # results = db.session.query(Temperature).filter(Temperature.Country != "").all()
    # cols = column_names(Temperature)

    # avgTemps = [{col: getattr(row, col) for col in cols} for row in results]

    # return render_template("index.html", data=avgTemps, columns=cols)
    return render_template("index.html")


@app.route("/api/temperatures")
def temperatures():
	
	return jsonify(get_data())

@app.route("/countries/<countryName>")
def country_data(countryName):

	return jsonify(temp_by_country()) 


if __name__ == "__main__":
    app.run(debug=True)