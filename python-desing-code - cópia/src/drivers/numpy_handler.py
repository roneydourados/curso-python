import numpy
from typing import List
from src.drivers.interfaces.driver_handler_interface import DriverHanleInterface

class NumpyHandler(DriverHanleInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers) # std é o método utilizado pela lib do numpy

    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)
