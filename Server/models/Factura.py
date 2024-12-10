from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                     tls=True, tlsAllowInvalidCertificates=True)
db = client['Sistema']

class Factura:
    def __init__(self, nombre_cliente, nombre_empleado, email, productos, costo_extras=0, total=0):
        self.nombre_cliente = nombre_cliente
        self.nombre_empleado = nombre_empleado
        self.email = email
        self.productos = productos
        self.costo_extras = costo_extras
        self.total = total
        self.timestamp = datetime.datetime.utcnow()

    def save(self):
        factura_data = {
            'nombreCliente': self.nombre_cliente,
            'nombreEmpleado': self.nombre_empleado,
            'email': self.email,
            'productos': self.productos,
            'costoExtras': self.costo_extras,
            'total': self.total,
            'createdAt': self.timestamp,
            'updatedAt': self.timestamp
        }
        db.facturas.insert_one(factura_data)

    @staticmethod
    def get_all():
        return db.facturas.find()

    @staticmethod
    def get_by_id(factura_id):
        return db.facturas.find_one({"_id": factura_id})

    @staticmethod
    def get_by_email(email):
        return db.facturas.find({"email": email})
