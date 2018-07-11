from pathlib import Path
from models import *

def fix_path(base, file_path):

    base = Path(base)
    Path(base / file_path)

    return str(Path(base / file_path).absolute())

def column_names(TableClass):
    names = map(lambda x: x.name, TableClass.__table__.columns)

    return list(names)

def table_filter(countryName):
    results = db.session.query(Temperature.Country).distinct().filter(Temperature.Country == "countryName")

    return results




