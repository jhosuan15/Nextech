# models/Inventario.py

from pymongo import MongoClient

client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                     tls=True, tlsAllowInvalidCertificates=True)
db = client['Sistema']
productos_collection = db['inventario']  # Conexión a la colección


class Producto:
    def __init__(self, nombre, descripcion, cantidad, precio, codigo_barras, imagen=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.codigo_barras = codigo_barras
        self.imagen = imagen

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'cantidad': self.cantidad,
            'precio': self.precio,
            'codigoBarras': self.codigo_barras,
            'imagen': self.imagen
        }

    def save(self):
        producto_data = self.to_dict()
        productos_collection.insert_one(producto_data)

    @staticmethod
    def get_all():
        productos = productos_collection.find()
        # Convertir los productos a diccionarios antes de retornarlos
        return [Producto(obj['nombre'], obj['descripcion'], obj['cantidad'], obj['precio'], obj['codigoBarras'], obj['imagen']).to_dict() for obj in productos]

    @staticmethod
    def get_by_id(producto_id):
        producto = productos_collection.find_one({"_id": producto_id})
        if producto:
            return Producto(producto['nombre'], producto['descripcion'], producto['cantidad'], producto['precio'], producto['codigoBarras'], producto['imagen']).to_dict()
        return None

   
    @staticmethod
    def update(nombre, data):
        # Buscar el producto por nombre y actualizarlo
        result = productos_collection.update_one({'nombre': nombre}, {'$set': data})
        
        # Verificar si la actualización fue exitosa
        if result.modified_count > 0:
            return True  # Si se actualizó al menos un producto
        return False  # Si no se actualizó ningún producto

    @staticmethod
    def delete(nombre):
        # Eliminar el producto por nombre
        result = productos_collection.delete_one({'nombre': nombre})
        
        # Verificar si la eliminación fue exitosa
        if result.deleted_count > 0:
            return True  # Si se eliminó al menos un producto
        return False  # Si no se eliminó ningún producto