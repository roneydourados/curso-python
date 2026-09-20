from typing import List

from sqlalchemy.orm.exc import NoResultFound

from ..entities.people import PeopleTable


class PeopleRepository:
    def __init__(self, db_connection_handler):
        self.db_connection_handler = db_connection_handler

    def get_all_people(self) -> List:
        with self.db_connection_handler as db:
            try:
                people = db.session.query(PeopleTable).all()
                return people
            except NoResultFound:
                return []

    def create_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.db_connection_handler as db:
            try:
                new_person = PeopleTable(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_id=pet_id,
                )
                db.session.add(new_person)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex

    def update_person(
        self, person_id: int, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.db_connection_handler as db:
            try:
                db.session.query(PeopleTable).filter_by(id=person_id).update(
                    {
                        "first_name": first_name,
                        "last_name": last_name,
                        "age": age,
                        "pet_id": pet_id,
                    }
                )
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex

    def delete_people(self, first_name: str) -> None:
        with self.db_connection_handler as db:
            try:
                person = (
                    db.session.query(PeopleTable).filter_by(first_name=first_name).first()
                )
                if person:
                    db.session.delete(person)
                    db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
