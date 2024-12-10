from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)
# Habilitar CORS para todas las rutas
CORS(app)
# Configurar la conexión a MongoDB
client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                     tls=True, tlsAllowInvalidCertificates=True)

db = client["Sistema"]

# Rutas para la colección "api TSE"
@app.route('/personas/<cedula>', methods=['GET'])
def obtener_persona(cedula):
    print(f"GET /personas/{cedula}")  # Log del GET en consola
    persona = db.personas.find_one({"cedula": cedula}, {"_id": 0})
    
    if persona:
        print(f"Respuesta: {persona}")  # Log de la respuesta exitosa
        return jsonify(persona), 200
    
    print("Respuesta: Persona no encontrada")  # Log de respuesta de error
    return jsonify({"error": "Persona no encontrada"}), 404

# Endpoint para obtener el precio de un producto API
@app.route('/productos/<nombre>', methods=['GET'])
def obtener_producto(nombre):
    producto = db.productos.find_one({"nombre": nombre}, {"_id": 0})
    
    if producto:
        print(f"Respuesta: {producto}")  # Log de la respuesta exitosa
        return jsonify(producto), 200
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

# Rutas para la colección "transacciones"  api BANCO
@app.route('/transacciones', methods=['POST'])
def insertar_transaccion():
    datos = request.json
    if not datos or not all(k in datos for k in ("numero_tarjeta", "monto")):
        return jsonify({"error": "Datos incompletos"}), 400
    
    transaccion = {
        "numero_tarjeta": datos["numero_tarjeta"],
        "monto": datos["monto"]
    }
    db.transacciones.insert_one(transaccion)
    return jsonify({"mensaje": "Transacción insertada con éxito"}), 201


if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.130', port=5002)  # Cambia host según la IP deseada































@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    usuario = datos.get('usuario')  # Asegúrate de que sea 'usuario'
    
    if not usuario:
        return jsonify({'error': 'El campo "usuario" es requerido'}), 400

    # Aquí verifica si el usuario existe en la base de datos
    usuario_db = db.usuarios.find_one({"usuario": usuario}, {"_id": 0})
    
    if usuario_db:
        return jsonify({'message': 'Autenticación exitosa', 'usuario': usuario_db}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
        