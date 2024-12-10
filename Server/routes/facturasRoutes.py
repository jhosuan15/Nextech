from flask import Blueprint, request, jsonify
from models.Factura import Factura
from bson import ObjectId

facturas_blueprint = Blueprint('facturas', __name__)

@facturas_blueprint.route('/', methods=['GET'])
def obtener_facturas():
    try:
        facturas = list(Factura.find())
        return jsonify(facturas), 200
    except Exception as error:
        return jsonify({"message": str(error)}), 500

@facturas_blueprint.route('/', methods=['POST'])
def crear_factura():
    data = request.get_json()
    factura = Factura(
        nombreCliente=data.get('nombreCliente'),
        nombreEmpleado=data.get('nombreEmpleado'),
        email=data.get('email'),
        productos=data.get('productos', []),
        costoExtras=data.get('costoExtras', 0),
        total=data.get('total', 0),
    )
    try:
        nueva_factura_id = factura.save()
        return jsonify(str(nueva_factura_id)), 201
    except Exception as error:
        return jsonify({"message": str(error)}), 400

@facturas_blueprint.route('/<id>', methods=['GET'])
def obtener_factura(id):
    try:
        factura = Factura.find_by_id(ObjectId(id))
        if factura is None:
            return jsonify({"message": "Factura no encontrada"}), 404
        return jsonify(factura), 200
    except Exception as error:
        return jsonify({"message": str(error)}), 500

@facturas_blueprint.route('/<id>', methods=['PUT'])
def actualizar_factura(id):
    data = request.get_json()
    try:
        factura = Factura.find_by_id(ObjectId(id))
        if factura is None:
            return jsonify({"message": "Factura no encontrada"}), 404

        factura['nombreCliente'] = data.get('nombreCliente', factura['nombreCliente'])
        factura['nombreEmpleado'] = data.get('nombreEmpleado', factura['nombreEmpleado'])
        factura['email'] = data.get('email', factura['email'])
        factura['productos'] = data.get('productos', factura['productos'])
        factura['costoExtras'] = data.get('costoExtras', factura['costoExtras'])
        factura['total'] = data.get('total', factura['total'])

        factura_actualizada = factura.save()
        return jsonify(factura_actualizada), 200
    except Exception as error:
        return jsonify({"message": str(error)}), 400

@facturas_blueprint.route('/<id>', methods=['DELETE'])
def eliminar_factura(id):
    try:
        factura = Factura.find_by_id(ObjectId(id))
        if factura is None:
            return jsonify({"message": "Factura no encontrada"}), 404

        factura.delete()
        return jsonify({"message": "Factura eliminada"}), 200
    except Exception as error:
        return jsonify({"message": str(error)}), 500
