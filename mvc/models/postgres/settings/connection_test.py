from sqlalchemy.engine import Engine
from .connection import db_connection_handler


def test_create_database_engine():
    engine = db_connection_handler.get_egine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_egine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
