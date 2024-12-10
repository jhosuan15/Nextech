# routes/usuarioRoutes.py

from flask import Blueprint, request
from controllers.usuarioController import get_usuarios, create_usuario, update_usuario, delete_usuario, login_usuario

usuarios_blueprint = Blueprint('usuarios', __name__)

# Definir las rutas y asociarlas con las funciones del controlador
@usuarios_blueprint.route('/', methods=['GET'])
def obtener_usuarios():
    return get_usuarios()

@usuarios_blueprint.route('/', methods=['POST'])
def crear_usuario():
    return create_usuario()

@usuarios_blueprint.route('/<usuario>', methods=['PUT'])
def actualizar_usuario(usuario):
    data = request.json
    return update_usuario(usuario, data)

@usuarios_blueprint.route('/<usuario>', methods=['DELETE'])
def eliminar_usuario(usuario):
    return delete_usuario(usuario)

@usuarios_blueprint.route('/login', methods=['POST'])
def login():
    return login_usuario()