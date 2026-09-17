from sqlalchemy import create_engine

class DBConnectiionHandler:
    def __init__(self):
        self.__connection_string = "postgresql://postgres:postgres@localhost:5432/curso_python"
        self.__engine = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_egine(self):
        return self.__engine

db_connection_handler = DBConnectiionHandler()