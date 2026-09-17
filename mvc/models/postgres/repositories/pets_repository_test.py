from unittest import mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from ..entities.pets import PetsTable
from .pets_repository import PetsRepository


class MockConnectionHandler:
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_all_pets():
    mock_pets = [
        PetsTable(id=1, name="rex", type="dog"),
        PetsTable(id=2, name="mimi", type="cat"),
    ]
    mock_session = UnifiedAlchemyMagicMock(
        data=[
            (
                [mock.call.query(PetsTable)],
                mock_pets,
            )
        ]
    )
    repo = PetsRepository(MockConnectionHandler(mock_session))

    response = repo.get_all_pets()

    assert len(response) == 2
    assert response[0].name == "rex"
    assert response[1].name == "mimi"

    print(response)


def test_create_pet():
    mock_session = UnifiedAlchemyMagicMock()
    repo = PetsRepository(MockConnectionHandler(mock_session))

    repo.create_pet("belinha", "dog")

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()

    added_pet = mock_session.add.call_args[0][0]
    assert isinstance(added_pet, PetsTable)
    assert added_pet.name == "belinha"
    assert added_pet.type == "dog"


def test_update_pet():
    mock_session = UnifiedAlchemyMagicMock()
    repo = PetsRepository(MockConnectionHandler(mock_session))

    repo.update_pet(1, "jorgin", "hamster")

    mock_session.filter_by.assert_called_once_with(id=1)
    mock_session.update.assert_called_once_with({"name": "jorgin", "type": "hamster"})
    mock_session.commit.assert_called_once()


def test_delete_pets():
    mock_pet = PetsTable(id=7, name="belinha", type="dog")
    mock_session = UnifiedAlchemyMagicMock(
        data=[
            (
                [
                    mock.call.query(PetsTable),
                    mock.call.filter_by(name="belinha"),
                ],
                [mock_pet],
            )
        ]
    )
    repo = PetsRepository(MockConnectionHandler(mock_session))

    repo.delete_pets("belinha")

    mock_session.filter_by.assert_called_once_with(name="belinha")
    mock_session.delete.assert_called_once_with(mock_pet)
    mock_session.commit.assert_called_once()
