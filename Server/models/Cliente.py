from pymongo import MongoClient
from bson import ObjectId
import re

client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                     tls=True, tlsAllowInvalidCertificates=True)
db = client['Sistema']

class Cliente:
    def __init__(self, nombre, empresa, correo):
        self.nombre = nombre
        self.empresa = empresa
        self.correo = correo

    def save(self):
        if not re.match(r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$', self.correo):
            raise ValueError(f'{self.correo} no es un correo válido!')
        cliente_data = {
            'nombre': self.nombre,
            'empresa': self.empresa,
            'correo': self.correo
        }
        db.clientes.insert_one(cliente_data)

    @staticmethod
    def get_all():
        return db.clientes.find()

    @staticmethod
    def get_by_id(cliente_id):
        return db.clientes.find_one({"_id": ObjectId(cliente_id)})

    @staticmethod
    def get_by_email(correo):
        return db.clientes.find_one({"correo": correo})
