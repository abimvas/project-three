from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func, types, Table
import re
from sqlalchemy.dialects.sqlite import DATE
import csv
from os import path
from utils import fix_path
from sqlalchemy.orm import Session
from sqlalchemy.types import DECIMAL
import pandas as pd
from datetime import datetime


db = SQLAlchemy()
# db.reflect(bind="finalDB")

# d = DATE(
#     storage_format = "%(year)04d-%(month)02d-%(day)02d",
#     regexp = re.compile("^[0-9]{4}-(((0[13578]|(10|12))-(0[1-9]|[1-2][0-9]|3[0-1]))|(02-(0[1-9]|[1-2][0-9]))|((0[469]|11)-(0[1-9]|[1-2][0-9]|30)))$")
#     )

base_path = path.abspath(path.dirname(__file__))

# Define a base model for other database tables to inherit
class Base01(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    date_modified = db.Column(
        db.Text,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

class Base02(db.Model):
    __abstract__ = True

    __table_args__ = {'sqlite_autoincrement': True}

    
    event_id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, default=db.func.current_timestamp())
    Yr = db.Column(db.Integer)
    M = db.Column(db.Integer)
    D = db.Column(db.Integer)
    City = db.Column(db.Text, index=True)
    Country = db.Column(db.Text)
    AvgTemp = db.Column(db.Float)
    AvgTUncert = db.Column(db.Float)
    Lat = db.Column(db.Float)
    Lat_Coord = db.Column(db.Float)
    Lat_Dir = db.Column(db.Float)
    Lon = db.Column(db.Float)
    Lng_Coord = db.Column(db.Float)
    Lng_Dir = db.Column(db.Float)
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

    __table_args__ = {'sqlite_autoincrement': True}

    __tablename__ = "locations"

    event_id = db.Column(db.Integer, primary_key=True)
    # Date = db.Column(db.Text, default=db.func.current_timestamp())
    Yr = db.Column(db.Integer)
    M = db.Column(db.Integer)
    D = db.Column(db.Integer)
    City = db.Column(db.Text)
    Country = db.Column(db.Text)
    AvgTemp = db.Column(db.Float)
    AvgTUncert = db.Column(db.Float)
    Lat = db.Column(db.Float)
    Lat_Coord = db.Column(db.Float) 
    Lat_Dir = db.Column(db.Text)
    Lon = db.Column(db.Float)
    Lng_Coord = db.Column(db.Float)
    Lng_Dir = db.Column(db.Text)

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


# def create_table(name, csvfile, db_uri):
#     engine = create_engine(db_uri, echo=True)
#     conn = engine.connect()
#     trans = conn.begin()
#     db.metadata.create_all(bind=engine)


#     with open(fix_path(base_path, csvfile), mode="r") as p:
#         csv_data = csv.DictReader(p)
        
         
#         for csvfile in csvfiles:
#         	try:

#                 for row in csv_data:
                    
#                     conn.execute(config.__table__.insert(), row)
#                 elif csvfile == 'db/avgGlobalTempsClean.csv':
#                         conn.execute(Location.__table__.insert(), row)
#             trans.commit()
#             except:
#                 trans.rollback()
#                 raise
#     tables = ['temperatures', 'locations']
#     for _t in tables: create_table(_t, metadata)




def create_table(csvfile, db_uri):
    engine = create_engine(db_uri, echo=True)
    conn = engine.connect()
    trans = conn.begin()
    db.metadata.create_all(engine)

    with open(fix_path(base_path, csvfile), mode="r") as p:
        csv_data = csv.DictReader(p)
        try:
            for row in csv_data:
                conn.execute(Temperature.__table__.insert(), row)
            trans.commit()
        except:
            trans.rollback()
            raise
