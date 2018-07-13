from flask import Flask, render_template, jsonify, json, request
from models import *
from sqlalchemy.orm import Session
from utils import *
from config import config
import os
import numpy as np
import plotly
import csv

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

# with app.app_context():
    
    

#     tables = ['temperatures', 'locations']
#     csvfiles = {'db/yearlytempavg1800.csv': app.config["SQLALCHEMY_DATABASE_URI"],
#             'db/avgGlobalTempsClean.csv': app.config["SQLALCHEMY_BINDS"]}
#     routes = create_table(**csvfiles)
    

#     for _t in tables, (csvfile, db_uri in csvfiles): 
#     	if not db.engine.dialect.has_table(db.engine, _t):
# 		    create_table(routes)

with app.app_context():
    if not db.engine.dialect.has_table(db.engine, "temperatures"):
        create_table("db/yearlytempavg1800.csv", app.config["SQLALCHEMY_DATABASE_URI"])
    elif not db.engine.dialect.has_table(db.engine, "locations"):
        create_table("db/avgGlobalTempsClean.csv", app.config["SQLALCHEMY_DATABASE_URI"])

#################################################
# Routes
#################################################

@app.before_first_request
def setup():

    db.create_all()

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