import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from theves.schema.declarative_base import Base
from theves.util import create_db_url
from fdb import fbcore


@pytest.fixture(scope="session")
def db_connection(tmpdir_factory):
    print(tmpdir_factory.getbasetemp())
    test_db_filename = tmpdir_factory.mktemp('test_sgs_schema').join('test.fdb').strpath
    fbcore.create_database(database=str(test_db_filename), user="SYSDBA", password="masterkey", page_size=8192)

    engine = create_engine(create_db_url("firebird", test_db_filename), encoding="latin1")
    connection = engine.connect()
    Base.metadata.create_all(engine)
    yield connection
    Base.metadata.drop_all(engine)
    connection.close()
    engine.dispose()


# noinspection PyShadowingNames
@pytest.fixture(scope="function")
def db_session(db_connection):
    trans = db_connection.begin()
    session = Session(bind=db_connection)
    yield session
    trans.rollback()
