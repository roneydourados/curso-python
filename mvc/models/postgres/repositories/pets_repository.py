from typing import List

from sqlalchemy.orm.exc import NoResultFound

from ..entities.pets import PetsTable
from ..settings.connection import DBConnectiionHandler


class PetsRepository:
    def __init__(self, db_connection_handler: DBConnectiionHandler):
        self.db_connection_handler = db_connection_handler

    def get_all_pets(self) -> List:
        with self.db_connection_handler as db:
            try:
                pets = db.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def create_pet(self, name: str, type: str) -> None:
        with self.db_connection_handler as db:
            try:
                new_pet = PetsTable(name=name, type=type)
                db.session.add(new_pet)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex

    def update_pet(self, pet_id: int, name: str, type: str) -> None:
        with self.db_connection_handler as db:
            try:
                db.session.query(PetsTable).filter_by(id=pet_id).update(
                    {"name": name, "type": type}
                )
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex

    def delete_pets(self, name: str) -> None:
        with self.db_connection_handler as db:
            try:
                pet = db.session.query(PetsTable).filter_by(name=name).first()
                if pet:
                    db.session.delete(pet)
                    db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
