from typing import Dict, List
import pytest
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHanleInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHanle(DriverHanleInterface):
    def __init__(self, variance_result: float = 3) -> None:
        self.__variance_result = variance_result

    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

    def variance(self, numbers: List[float]) -> float:
        return self.__variance_result


def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)
    response = calculator_3.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {
        "data": {
            "calculator": 3,
            "variance": 1.98,
            "multiplication": 12.93,
            "success": True,
        }
    }


def test_calculate_with_success():
    mock_request = MockRequest(body={"numbers": [2, 3, 4]})

    driver = MockDriverHanle(variance_result=3)
    calculator_3 = Calculator3(driver)
    response = calculator_3.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {
        "data": {
            "calculator": 3,
            "variance": 3,
            "multiplication": 24,
            "success": True,
        }
    }


def test_calculate_with_failure():
    mock_request = MockRequest(body={"numbers": [1, 1, 1]})

    driver = MockDriverHanle(variance_result=3)
    calculator_3 = Calculator3(driver)

    with pytest.raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Falha no processo: Variância é Maior que a multiplicação!"


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": [2.12, 4.62, 1.32]})

    driver = MockDriverHanle()
    calculator_3 = Calculator3(driver)

    with pytest.raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "O corpo da requisição requer uma lista de números."
    print(excinfo.value)
