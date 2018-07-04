from flask import Flask, render_template, jsonify
from models import db, Temperature, Temps_Since_1800
from sqlalchemy.orm import Session
from utils import column_names
from config import config
import os
import numpy as np


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

    results = db.session.query(Temperature).filter(Temperature.Country != "").all()
    cols = column_names(Temperature)

    avgTemps = [{col: getattr(row, col) for col in cols} for row in results]

    return render_template("index.html", data=avgTemps, columns=cols)

@app.route("/api/temperatures")
def temperatures():
    q = [Temperature.id, Temperature.Country, Temperature.year, Temperature.AverageTemperatureF]
    # avgTemps = []
    results = db.session.query(*q).all()

    # for result in results:
    #     temp_dict = {}
    #     for col in Temperature.__table__.columns:
    #         d = getattr(result, col.name)
    #         if isinstance(d, decimal.Decimal): d = float(d);
    #         temp_dict[col.name] = d
    #     avgTemps.append(temp_dict)
   
    # return jsonify(Temps)

    cols = list(map(lambda x: x["name"], results.column_descriptions))
    # cols = column_names(Temperature)
    avgTemps = {
        "data": [
            {col: getattr(row, col) for col in cols} for row in results.all()
        ]
    }
    return jsonify(avgTemps)
     


if __name__ == "__main__":
    app.run()