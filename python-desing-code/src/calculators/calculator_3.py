from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHanleInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError


class Calculator3:
    def __init__(self, driver_handle: DriverHanleInterface):
        self.__driver_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        #Fazer a validação do resultado
        self.__verify_result(variance, multiplication)

        formated_response = self.__formated_response(variance, multiplication)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError('O corpo da requisição requer uma lista de números.')

        input_data = body['numbers']
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handle.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for number in numbers: multiplication *= number

        return multiplication

    def __verify_result (self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError('Falha no processo: Variância é Maior que a multiplicação!')


    def __formated_response(self, variance: float, multiplication: float) -> Dict:
       return {
           "data":{
               "calculator": 3,
               "variance": round(variance, 2),
               "multiplication": round(multiplication, 2),
               "success": True,
           }
       }