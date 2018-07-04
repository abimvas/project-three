from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import csv
from os import path
from utils import fix_path
from sqlalchemy.orm import Session
from sqlalchemy.types import DECIMAL

db = SQLAlchemy()
base_path = path.abspath(path.dirname(__file__))

# Define a base model for other database tables to inherit
class Base(db.Model):
	__abstract__  = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.Text, default=db.func.current_timestamp())
	date_modified = db.Column(
    	db.Text,
    	default=db.func.current_timestamp(),
    	onupdate=db.func.current_timestamp()
	)

class Temperature(Base):

	__tablename__ = "temperatures"

	id = db.Column(db.Integer, primary_key=True)
	Country = db.Column(db.Text)
	year = db.Column(db.Integer)
	AverageTemperatureF = db.Column(db.Float)

	def __repr__(self):
		return '<Temperature %r>' % (self.AverageTemperatureF)

def Temps_Since_1800(csvfile, db_uri):
	engine = create_engine(db_uri, echo=False)
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
		
