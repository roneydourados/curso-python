from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from types import TracebackType


class DBConnectiionHandler:
    def __init__(self):
        self.__connection_string = "postgresql://postgres:postgres@localhost:5432/curso_python"
        self.__engine = None
        self.session = None
    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)
    def get_egine(self):
        return self.__engine
    def __enter__(self):
        session_make = sessionmaker()
        self.session = session_make(bind=self.__engine)
        return self
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        self.session.close()

db_connection_handler = DBConnectiionHandler()