from typing import Dict
import pytest
from .calculator_1 import Calculator1


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calulate(mock_request)

    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["calculator"] == 1
    assert response["data"]["result"] == 14.25

    print(response)


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with pytest.raises(Exception) as excinfo:
        calculator_1.calulate(mock_request)

    assert str(excinfo.value) == "O corpo da requisição requer um número."
    print(excinfo.value)
