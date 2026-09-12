from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

def calcultor3_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    return calc