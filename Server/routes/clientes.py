from flask import Blueprint, request, jsonify
from controllers.ClienteController import crear_cliente

clientes_blueprint = Blueprint('clientes', __name__)

@clientes_blueprint.route('/', methods=['POST'])
def crear_cliente_route():
    return crear_cliente()
