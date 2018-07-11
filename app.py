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

with app.app_context():
	if not db.engine.dialect.has_table(db.engine, "locations"):
		Temps_Since_1800("db/final.csv", app.config["SQLALCHEMY_BINDS"])



#################################################
# Routes
#################################################

@app.before_first_request
def setup():
    # db.drop_all()
    db.create_all()
    db.create_all(bind='finalDB')

@app.route("/")
def index():

    results = db.session.query(Temperature.Country).distinct().all()
    results = [c.Country for c in results]
    print(results)

    return render_template("index.html", countries=results)


@app.route("/api/temperatures")
def temperatures():

	return jsonify(get_data())


@app.route("/countries")
@app.route("/countries/<countryName>")
def country_data(countryName):

	return jsonify(temp_by_country(countryName)) 


if __name__ == "__main__":
    app.run(debug=True)