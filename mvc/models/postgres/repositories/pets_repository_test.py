import pytest
from unittest import mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from ..entities.pets import PetsTable
from .pets_repository import PetsRepository

from sqlalchemy.orm.exc import NoResultFound


class MockConnectionHandler:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(id=1, name="rex", type="dog"),
                        PetsTable(id=2, name="mimi", type="cat"),
                    ],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class MockConnectionHandlerNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("Result not found!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_all_pets():
    mock_connection = MockConnectionHandler()
    repo = PetsRepository(mock_connection)

    response = repo.get_all_pets()

    assert len(response) == 2
    assert response[0].name == "rex"
    assert response[1].name == "mimi"

    print(response)


def test_create_pet():
    mock_connection = MockConnectionHandler()
    repo = PetsRepository(mock_connection)

    repo.create_pet("belinha", "dog")

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

    added_pet = mock_connection.session.add.call_args[0][0]
    assert isinstance(added_pet, PetsTable)
    assert added_pet.name == "belinha"
    assert added_pet.type == "dog"


def test_update_pet():
    mock_connection = MockConnectionHandler()
    repo = PetsRepository(mock_connection)

    repo.update_pet(1, "jorgin", "hamster")

    mock_connection.session.filter_by.assert_called_once_with(id=1)
    mock_connection.session.update.assert_called_once_with(
        {"name": "jorgin", "type": "hamster"}
    )
    mock_connection.session.commit.assert_called_once()


def test_delete_pets():
    mock_connection = MockConnectionHandler()
    repo = PetsRepository(mock_connection)

    repo.delete_pets("rex")

    mock_connection.session.filter_by.assert_called_once_with(name="rex")
    mock_connection.session.delete.assert_called_once()
    deleted_pet = mock_connection.session.delete.call_args[0][0]
    assert deleted_pet.name == "rex"
    mock_connection.session.commit.assert_called_once()

def test_get_all_pets_not_result():
    mock_connection = MockConnectionHandlerNoResult()
    repo = PetsRepository(mock_connection)
    resp = repo.get_all_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert resp == []

def test_delete_pets_no_result():
    mock_connection = MockConnectionHandlerNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pets("lala")