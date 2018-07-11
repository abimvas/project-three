from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
import csv
from os import path
from utils import fix_path
from sqlalchemy.orm import Session
from sqlalchemy.types import DECIMAL
import pandas as pd


db = SQLAlchemy()
# db.reflect(bind="finalDB")

base_path = path.abspath(path.dirname(__file__))
 

# Define a base model for other database tables to inherit
class Base01(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Text, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.Text,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

class Base02(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    date = db.Column(db.String)
    AverageTemperatureF = db.Column(db.Float)
    AverageTemperature = db.Column(db.Float)
    AverageTemperatureUncertainty = db.Column(db.Float)
    City = db.Column(db.Text)
    Country = db.Column(db.Text)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    year = db.Column(db.Integer)
    # date_created = db.Column(db.Text, default=db.func.current_timestamp())
    # date_modified = db.Column(
    #     db.Text,
    #     default=db.func.current_timestamp(),
    #     onupdate=db.func.current_timestamp()
    # )

class Temperature(Base01):
    __tablename__ = "temperatures"

    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.Text)
    year = db.Column(db.Integer)
    AverageTemperatureF = db.Column(db.Float)

    def __repr__(self):
        return '<Temperature %r>' % (self.AverageTemperatureF)


class Location(Base02):
    __bind_key__ = "finalDB"

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, default=db.func.current_timestamp())
    AverageTemperatureF = db.Column(db.Float)
    AverageTemperature = db.Column(db.Float)
    AverageTemperatureUncertainty = db.Column(db.Float)
    City = db.Column(db.Text)
    Country = db.Column(db.Text)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    year = db.Column(db.Integer)

    def __repr__(self):
        return '<City %r>' % (self.City)



def get_data():
    q = [Temperature.id, Temperature.Country, Temperature.year, Temperature.AverageTemperatureF]
    avgTemps = db.session.query(
        *q,
        func.max(Temperature.AverageTemperatureF).label("High"),
        func.min(Temperature.AverageTemperatureF).label("Low"),
        (func.max(Temperature.AverageTemperatureF) - func.min(Temperature.AverageTemperatureF)).\
        label("Difference")).group_by(Temperature.Country).all()

    print(avgTemps)
    return avgTemps

def temp_by_country(countryName):   
    q = [Temperature.Country, Temperature.AverageTemperatureF]
    results = db.session.query(
        *q,
        func.max(Temperature.AverageTemperatureF).label("High"),
        func.min(Temperature.AverageTemperatureF).label("Low"),
        (func.max(Temperature.AverageTemperatureF) - func.min(Temperature.AverageTemperatureF)).\
        label("Difference")).group_by(Temperature.Country)\
    .filter(Temperature.Country.like(f"%{countryName}%")).all()

    return results


def Temps_Since_1800(csvfile, db_uri):
    engine = create_engine(db_uri, echo=True)
    conn = engine.connect()
    trans = conn.begin()
    db.metadata.create_all(engine)
    # db.reflect(bind="finalDB")

    with open(fix_path(base_path, csvfile), mode="r") as p:
        csv_data = csv.DictReader(p)

        try:
            for row in csv_data:
                if csvfile == 'db/yearlytempavg1800.csv':
                    conn.execute(Temperature.__table__.insert(), row)
                elif csvfile == 'db/final.csv':
                    conn.execute(Location.__table__.insert(), row)
            trans.commit()
        except:
            trans.rollback()
            raise



# def Temps_Since_1800(csvfile, db_uri):
#     engine = create_engine(db_uri, echo=True)
#     conn = engine.connect()
#     trans = conn.begin()
#     db.metadata.create_all(engine)

#     with open(fix_path(base_path, csvfile), mode="r") as p:
#         csv_data = csv.DictReader(p)
#         try:
#             for row in csv_data:
#                 conn.execute(Temperature.__table__.insert(), row)
#             trans.commit()
#         except:
#             trans.rollback()
#             raise
