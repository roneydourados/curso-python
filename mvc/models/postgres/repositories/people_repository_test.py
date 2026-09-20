import pytest
from unittest import mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from ..entities.people import PeopleTable
from .people_repository import PeopleRepository

from sqlalchemy.orm.exc import NoResultFound


class MockConnectionHandler:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PeopleTable)],
                    [
                        PeopleTable(
                            id=1,
                            first_name="john",
                            last_name="doe",
                            age=30,
                            pet_id=1,
                        ),
                        PeopleTable(
                            id=2,
                            first_name="jane",
                            last_name="doe",
                            age=25,
                            pet_id=2,
                        ),
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


def test_get_all_people():
    mock_connection = MockConnectionHandler()
    repo = PeopleRepository(mock_connection)

    response = repo.get_all_people()

    assert len(response) == 2
    assert response[0].first_name == "john"
    assert response[1].first_name == "jane"

    print(response)


def test_create_person():
    mock_connection = MockConnectionHandler()
    repo = PeopleRepository(mock_connection)

    repo.create_person("bob", "smith", 40, 1)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

    added_person = mock_connection.session.add.call_args[0][0]
    assert isinstance(added_person, PeopleTable)
    assert added_person.first_name == "bob"
    assert added_person.last_name == "smith"
    assert added_person.age == 40
    assert added_person.pet_id == 1


def test_update_person():
    mock_connection = MockConnectionHandler()
    repo = PeopleRepository(mock_connection)

    repo.update_person(1, "johnny", "doe", 31, 2)

    mock_connection.session.filter_by.assert_called_once_with(id=1)
    mock_connection.session.update.assert_called_once_with(
        {
            "first_name": "johnny",
            "last_name": "doe",
            "age": 31,
            "pet_id": 2,
        }
    )
    mock_connection.session.commit.assert_called_once()


def test_delete_people():
    mock_connection = MockConnectionHandler()
    repo = PeopleRepository(mock_connection)

    repo.delete_people("john")

    mock_connection.session.filter_by.assert_called_once_with(first_name="john")
    mock_connection.session.delete.assert_called_once()
    deleted_person = mock_connection.session.delete.call_args[0][0]
    assert deleted_person.first_name == "john"
    mock_connection.session.commit.assert_called_once()


def test_get_all_people_not_result():
    mock_connection = MockConnectionHandlerNoResult()
    repo = PeopleRepository(mock_connection)
    resp = repo.get_all_people()

    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert resp == []


def test_delete_people_no_result():
    mock_connection = MockConnectionHandlerNoResult()
    repo = PeopleRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_people("lala")
