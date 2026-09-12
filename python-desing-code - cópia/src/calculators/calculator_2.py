from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHanleInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator2:
    def __init__(self, driver_handle: DriverHanleInterface):
        self.__driver_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        imput_data = self.__validate_body(body)
        calculated_number = self.__process_data(imput_data)
        formated_response = self.__formated_response(calculated_number)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError('O corpo da requisição requer uma lista de números.')

        input_data = body['numbers']
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
       first_process_result = [(num * 11) ** 0.95 for num in input_data]
       result = self.__driver_handle.standard_derivation(first_process_result)
       return 1/result

    def __formated_response(self, calc_result: float) -> Dict:
       return {
           "data":{
               "calculator": 2,
               "result": round(calc_result, 2)
           }
       }

