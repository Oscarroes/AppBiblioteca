class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.fs = modelo.fs

    def botonPresionado(self):
        print("Botón presionado")

        datos = self.modelo.consultarDatos()

        for dato in datos:
            print(dato)

    def traerLibro(self, titulo):
        libro = self.modelo.traerLibroPorTitulo(titulo)
        return libro
    def obtenerPortada(self, idPortada):
        return self.modelo.obtenerPortada(idPortada)

    def guardarInfo(self, titulo, autor, datosImagen):
        # Guardar la imagen en GridFS
        idPortada = self.fs.put(datosImagen, filename='portada.png')
        self.modelo.guardarLibro(titulo, autor, idPortada)
        print("libro guardado correctamente")
