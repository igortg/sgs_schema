import os


def create_db_url(db_type, db_path, user="sysdba", password="masterkey"):
    if os.path.isfile(db_path):
        db_path = db_path.replace("\\", "/").replace(":", "/")
    return "{}://{}:{}@{}".format(db_type, user, password, db_path)
