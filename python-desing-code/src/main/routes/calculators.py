from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calcultor2_factory
from src.main.factories.calculator3_factory import calcultor3_factory
from src.errors.error_controller import handle_errors

calc_route_bp = Blueprint('calc_route', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator():
    try:
        calc = calculator1_factory()
        response = calc.calulate(request)
        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"], error_response["status_code"])

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator2():
    try:
        calc = calcultor2_factory()
        response = calc.calculate(request)
        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"], error_response["status_code"])

@calc_route_bp.route('/calculator/3', methods=['POST'])
def calculator3():
    try:
        calc = calcultor3_factory()
        response = calc.calculate(request)
        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"], error_response["status_code"])
