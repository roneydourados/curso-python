from models.postgres.interfaces.people_repository_interface import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, peopleRepository: PeopleRepositoryInterface) -> None:
        self.__peopleRepository = peopleRepository
        pass