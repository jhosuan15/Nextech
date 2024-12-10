from flask import Flask, request, jsonify
from pymongo import MongoClient
import re

app = Flask(__name__)

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", tls=True, tlsAllowInvalidCertificates=True)
db = client['Sistema']
clientes_collection = db['clientes']

# Ruta para crear un nuevo cliente
@app.route('/api/crear-cliente', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    nombre = data.get('nombre')
    empresa = data.get('empresa')
    correo = data.get('correo')

    # Validación del correo
    if not re.match(r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$', correo):
        return jsonify({'mensaje': 'Correo electrónico no válido'}), 400

    # Verificar si ya existe un cliente con el mismo correo
    cliente_existente = clientes_collection.find_one({'correo': correo})
    if cliente_existente:
        return jsonify({'mensaje': 'Ya existe un cliente con ese correo electrónico'}), 400

    # Crear un nuevo cliente
    nuevo_cliente = {
        'nombre': nombre,
        'empresa': empresa,
        'correo': correo
    }

    try:
        # Insertar el nuevo cliente en la base de datos
        cliente_guardado = clientes_collection.insert_one(nuevo_cliente)
        nuevo_cliente['_id'] = str(cliente_guardado.inserted_id)  # Agregar el _id generado
        return jsonify(nuevo_cliente), 201
    except Exception as e:
        return jsonify({'mensaje': 'Error al guardar el cliente', 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
