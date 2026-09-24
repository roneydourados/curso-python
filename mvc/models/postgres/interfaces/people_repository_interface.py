from abc import ABC, abstractclassmethod
from typing import List

from models.postgres.entities.people import PeopleTable


class PeopleRepositoryInterface(ABC):
    @abstractclassmethod
    def get_all_people(self) -> List:
        pass

    @abstractclassmethod
    def create_person(
            self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        pass

    @abstractclassmethod
    def update_person(
        self, person_id: int, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        pass

    @abstractclassmethod
    def delete_people(self, first_name: str) -> None:
        pass

    @abstractclassmethod
    def get_person(self, person_id: int) -> PeopleTable:
        pass

