# controllers/usuarioController.py

from flask import jsonify, request
from models.Usuario import Usuario  # Importamos el modelo Usuario

# Ruta para obtener todos los usuarios
def get_usuarios():
    try:
        usuarios = Usuario.get_all()
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({'message': 'Error al obtener usuarios', 'error': str(e)}), 500

# Ruta para crear un nuevo usuario
def create_usuario():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')
    plazo = data.get('plazo')

    nuevo_usuario = Usuario(usuario, contrasena, plazo)

    try:
        nuevo_usuario.save()
        return jsonify({'message': 'Usuario creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'message': 'Error al crear el usuario', 'error': str(e)}), 500

# Ruta para actualizar un usuario
def update_usuario(usuario, data):
    try:
        actualizado = Usuario.update(usuario, data)
        
        if not actualizado:
            return jsonify({'message': 'Usuario no encontrado para actualizar'}), 404
        
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    
    except Exception as e:
        return jsonify({'message': 'Error al actualizar el usuario', 'error': str(e)}), 500

# Ruta para eliminar un usuario
def delete_usuario(usuario):
    try:
        eliminado = Usuario.delete(usuario)
        
        if not eliminado:
            return jsonify({'message': 'Usuario no encontrado para eliminar'}), 404
        
        return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
    
    except Exception as e:
        return jsonify({'message': 'Error al eliminar el usuario', 'error': str(e)}), 500

# Ruta para verificar usuario y contraseña
def login_usuario():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    if not usuario or not contrasena:
        return jsonify({'message': 'Por favor, proporciona un usuario y una contraseña'}), 400

    # Verificar la contraseña
    if Usuario.verify_password(usuario, contrasena):
        return jsonify({'message': 'Autenticación exitosa'}), 200
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401