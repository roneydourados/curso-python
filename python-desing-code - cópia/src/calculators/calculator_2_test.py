from typing import Dict, List
import pytest
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHanleInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHanle(DriverHanleInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

    def variance(self, numbers: List[float]) -> float:
        return 3


def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {"data": {'calculator': 2, 'result': 0.08}}


def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHanle()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {"data": {'calculator': 2, 'result': 0.33}}


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": [2.12, 4.62, 1.32]})

    driver = MockDriverHanle()
    calculator_2 = Calculator2(driver)

    with pytest.raises(Exception) as excinfo:
        calculator_2.calculate(mock_request)

    assert str(excinfo.value) == "O corpo da requisição requer uma lista de números."
    print(excinfo.value)
