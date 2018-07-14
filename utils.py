from pathlib import Path
from models import *

def fix_path(base, file_path):

    base = Path(base)
    Path(base / file_path)

    return str(Path(base / file_path).absolute())

def column_names(TableClass):
    names = map(lambda x: x.name, TableClass.__table__.columns)
    d = DATE(
        storage_format = "%(year)04d-%(month)02d-%(day)02d",
        regexp = re.compile("^[0-9]{4}-(((0[13578]|(10|12))-(0[1-9]|[1-2][0-9]|3[0-1]))|(02-(0[1-9]|[1-2][0-9]))|((0[469]|11)-(0[1-9]|[1-2][0-9]|30)))$")
    )

    return list(names)

def table_filter(countryName):
    results = db.session.query(Temperature.Country).distinct().filter(Temperature.Country == "countryName")

    return results




