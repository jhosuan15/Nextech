# inventarioController.py

from flask import jsonify, request
from models.Inventario import Producto  # Importamos el modelo Producto

# Ruta para obtener todos los productos
def get_productos():
    try:
        # Usamos el modelo para obtener los productos, ya convertidos a diccionarios
        productos = Producto.get_all()
        return jsonify(productos)
    except Exception as e:
        return jsonify({'message': 'Error al obtener productos', 'error': str(e)}), 500

# Ruta para crear un nuevo producto
def create_producto():
    data = request.get_json()
    codigo_barras = data.get('codigoBarras')
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    cantidad = data.get('cantidad')
    precio = data.get('precio')
    imagen = data.get('imagen')

    nuevo_producto = Producto(nombre, descripcion, cantidad, precio, codigo_barras, imagen)

    try:
        # Usamos el método del modelo para guardar el producto
        nuevo_producto.save()
        return jsonify({'message': 'Producto creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'message': 'Error al crear el producto', 'error': str(e)}), 500


# Ruta para actualizar un producto por nombre
def update_producto(nombre, data):
    try:
        actualizado = Producto.update(nombre, data)
        
        if not actualizado:
            return jsonify({'message': 'Producto no encontrado para actualizar'}), 404
        
        return jsonify({'message': 'Producto actualizado exitosamente'}), 200
    
    except Exception as e:
        return jsonify({'message': 'Error al actualizar el producto', 'error': str(e)}), 500

# Ruta para eliminar un producto por nombre
def delete_producto(nombre):
    try:
        eliminado = Producto.delete(nombre)
        
        if not eliminado:
            return jsonify({'message': 'Producto no encontrado para eliminar'}), 404
        
        return jsonify({'message': 'Producto eliminado exitosamente'}), 200
    
    except Exception as e:
        return jsonify({'message': 'Error al eliminar el producto', 'error': str(e)}), 500