import pymongo
import gridfs

class Modelo:
    def __init__(self):
        self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente["miBiblioteca"]
        self.coleccion = self.db["libros"]

        # Inicializar GridFS para almacenar la imagen en modo binario
        self.fs = gridfs.GridFS(self.db)

    def consultarDatos(self):
        resultados = self.coleccion.find()

        return resultados
    
    def guardarLibro(self,titulo, autor, idPortada):

        libro = {
            "titulo":titulo,
            "autor":autor,
            "portada":idPortada
            }
        self.coleccion.insert_one(libro)
        