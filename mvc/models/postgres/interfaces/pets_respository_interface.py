from abc import ABC, abstractclassmethod

from typing import List

class PetsRepositoryInterface(ABC):
    @abstractclassmethod
    def get_all_pets(self) -> List:
        pass

    @abstractclassmethod
    def create_pet(self, name: str, type: str) -> None:
        pass

    @abstractclassmethod
    def update_pet(self, pet_id: int, name: str, type: str) -> None:
        pass

    @abstractclassmethod
    def delete_pets(self, name: str) -> None:
        pass
