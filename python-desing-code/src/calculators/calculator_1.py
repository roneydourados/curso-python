from typing import Dict
from flask import Request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator1:
    """
    Um Número dividido em 3 partes

    a primeira parte é dividio por 4 e seu resultado é somado a 7
    após isso, o resultado é elevado ao quadrado e multiplicado por 0.257

    a segunda parte é elevada a potência 2.121, dividida por 5 e somado a 1

    a terceira parte mantem o memso valor

    final é mostrar a soma dos três valores
    """
    def calulate(self, request: FlaskRequest):
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        calculated_result = first_process_result + second_process_result + splited_number
        response = self.__forma_response(calculated_result)
        return response

    def __validate_body(self, body: Dict) -> float:
        if 'number' not in body:
            raise HttpUnprocessableEntityError('O corpo da requisição requer um número.')

        input_data = body['number']
        return input_data

    def __first_process (self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process (self, second_number: float) -> float:
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part

    def __forma_response(self, calc_result: float) -> Dict:
       return {
           "data":{
               "calculator": 1,
               "result": round(calc_result, 2)
           }
       }


