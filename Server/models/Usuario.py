import bcrypt
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                     tls=True, tlsAllowInvalidCertificates=True)
db = client['Sistema']
usuarios_collection = db['usuarios']  # Conexión a la colección de usuarios

class Usuario:
    def __init__(self, usuario, contrasena, plazo):
        self.usuario = usuario
        self.contrasena = contrasena
        self.plazo = plazo

    def to_dict(self):
        return {
            'usuario': self.usuario,
            'contrasena': self.contrasena,
            'plazo': self.plazo
        }

    def save(self):
        # Encriptar la contraseña antes de guardar
        hashed_password = bcrypt.hashpw(self.contrasena.encode('utf-8'), bcrypt.gensalt())
        self.contrasena = hashed_password
        usuario_data = self.to_dict()
        usuarios_collection.insert_one(usuario_data)

    @staticmethod
    def get_all():
        usuarios = usuarios_collection.find()
        return [Usuario(obj['usuario'], obj['contrasena'], obj['plazo']).to_dict() for obj in usuarios]

    @staticmethod
    def get_by_id(usuario_id):
        usuario = usuarios_collection.find_one({"_id": usuario_id})
        if usuario:
            return Usuario(usuario['usuario'], usuario['contrasena'], usuario['plazo']).to_dict()
        return None

    @staticmethod
    def update(usuario, data):
        result = usuarios_collection.update_one({'usuario': usuario}, {'$set': data})
        if result.modified_count > 0:
            return True
        return False

    @staticmethod
    def delete(usuario):
        result = usuarios_collection.delete_one({'usuario': usuario})
        if result.deleted_count > 0:
            return True
        return False

    @staticmethod
    def verify_password(usuario, contrasena):
        user = usuarios_collection.find_one({"usuario": usuario})
        if user:
            print("true")
            return True  # El usuario existe en la base de datos
        return False  # No se encontró el usuario
