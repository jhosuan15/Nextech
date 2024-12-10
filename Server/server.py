from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

try:
    # Conexión a MongoDB
    client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                         tls=True, tlsAllowInvalidCertificates=True)
    
    # Verificar la conexión
    client.server_info()  # Esto lanzará un error si la conexión falla
    print("Conexión exitosa a la base de datos MongoDB")

except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

db = client['Sistema']

# Importar y registrar los blueprints
from routes.inventarioRoutes import inventario_blueprint
from routes.facturasRoutes import facturas_blueprint
from routes.clientes import clientes_blueprint
from routes.usuarioRoutes import usuarios_blueprint
app.register_blueprint(inventario_blueprint, url_prefix='/api/inventario')
app.register_blueprint(facturas_blueprint, url_prefix='/api/facturas')
app.register_blueprint(clientes_blueprint, url_prefix='/api/clientes')
app.register_blueprint(usuarios_blueprint, url_prefix='/api/usuarios')


if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.130', port=5003)  # Cambia host según la IP deseada


