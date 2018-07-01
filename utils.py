from pathlib import Path

def fix_path(base, file_path):

    base = Path(base)
    Path(base / file_path)

    return str(Path(base / file_path).absolute())

def column_names(TableClass):
    names = map(lambda x: x.name, TableClass.__table__.columns)
    # names = {x.name: getattr(x,x.name) for x in TableClass.__table__.columns}

    return list(names)