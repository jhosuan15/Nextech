# inventarioRoutes.py

from flask import Blueprint, request
from controllers.inventarioController import get_productos, create_producto, update_producto, delete_producto

inventario_blueprint = Blueprint('inventario', __name__)

# Definir las rutas y asociarlas con las funciones del controlador
@inventario_blueprint.route('/', methods=['GET'])
def obtener_productos():
    return get_productos()

@inventario_blueprint.route('/', methods=['POST'])
def crear_producto():
    return create_producto()

@inventario_blueprint.route('/<nombre>', methods=['PUT'])
def actualizar_producto(nombre):
    data = request.json
    return update_producto(nombre,data)

@inventario_blueprint.route('/<nombre>', methods=['DELETE'])
def eliminar_producto(nombre):
    return delete_producto(nombre)
