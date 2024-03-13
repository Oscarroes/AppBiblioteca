from customtkinter import *
import tkinter as tk
from tkinter import filedialog
import os

class Vista:


    def __init__(self, controlador):
        self.controlador = controlador

        #----------------------------INTERFAZ GRÁFICA-----------------------------------------

        self.ventana = CTk()
        self.ventana.geometry("1024x640")
        self.ventana.configure(fg_color="#2E4C39")
        self.ventana.title('Mi Biblioteca')
        self.ventana.iconbitmap('img/iconoLibros.ico')
        
        # Variables
        self.imagenPath = tk.StringVar()

        # self.etiquetaTitulo = CTkLabel(master=self.ventana,text="Titulo")
        # self.etiquetaTitulo.grid(row=0, column=0, padx=10, pady=5)
        # self.entradaTitulo = CTkEntry(master=self.ventana)
        # self.entradaTitulo.grid(row=0, column=1, padx=10, pady=5)

        # self.etiquetaAutor = CTkLabel(master=self.ventana,text="Autor")
        # self.etiquetaAutor.grid(row=1, column=0, padx=10, pady=5)
        # self.entradaAutor = CTkEntry(master=self.ventana)
        # self.entradaAutor.grid(row=1, column=1, padx=10, pady=5)

        # self.etiquetaPortada = CTkLabel(master=self.ventana,text="Portada")
        # self.etiquetaPortada.grid(row=2, column=0, padx=10, pady=5)
        # self.entradaPortada = CTkEntry(master=self.ventana, textvariable=self.imagenPath, state="readonly")
        # self.entradaPortada.grid(row=2, column=2, padx=10, pady=5)

        # self.etiquetaBuscarTitulo = CTkLabel(master=self.ventana,text="Buscar por titulo")
        # self.etiquetaBuscarTitulo.grid(row=4, column=0, padx=10, pady=5)
        # self.entradaBuscarTitulo = CTkEntry(master=self.ventana)
        # self.entradaBuscarTitulo.grid(row=4, column=1, padx=10, pady=5)

        #-----------------------FAME CON MENU INICIAL-------------------------------------

        self.frameMenu = CTkFrame(master=self.ventana, width=925, height=50, fg_color="#F6FFF9", border_color="#636E67", border_width=3)
        # self.frameMenu.grid(row=0, column=0, padx=10, pady=10)
        self.frameMenu.place(relx=0.5, rely=0.1, anchor="center")

        #BOTÓN DE AGREGAR NUEVO LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="Nuevo libro",
                                command=self.guardarInfo,
                                text_color="#F6FFF9",
                                height=40,
                                width=150,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
            # self.boton.place(relx=0.2, rely=0.35, anchor="center")
        self.boton.grid(row=0, padx=10, pady=10)

        # #BOTÓN DE EXPLORACIÓN
        # self.botonExplorador = CTkButton(master=self.ventana,text="Abrir explorador", command=self.abrirExplorador)
        #     # self.botonExplorador.place(relx=0.8, rely=0.35, anchor="center")
        # self.botonExplorador.grid(row=2, column=1, padx=10, pady=5)

        # #BOTÓN CONSULTAR POR TÍTULO
        # self.botonTraerLibro = CTkButton(master=self.ventana, text="Traer Libro", corner_radius=32, fg_color="#C850C0",
        #    hover_color="#4158D0", border_color="#FFCC70", border_width=2, command=self.botonTraerLibroPulsado)
        # self.botonTraerLibro.grid(row=4, column=2, padx=10, pady=5)


        #-------------------------FRAME CON SCROLLBAR---------------------------------------------

        self.marcoLibros = CTkScrollableFrame(master=self.ventana,width=900, height=400, fg_color="#F6FFF9", border_color="#636E67", border_width=3,
                                orientation="vertical", scrollbar_button_color="#75CB92")
        # self.marcoLibros.grid(row=1, columnspan=4, padx=10, pady=10)
        self.marcoLibros.place(relx=0.5, rely=0.5, anchor="center")

        #-------------------------FRAME CON MENU FINAL---------------------------------------

        self.frameMenuFinal = CTkFrame(master=self.ventana, width=925, height=50, fg_color="#F6FFF9", border_color="#636E67", border_width=3)
        # self.frameMenu.grid(row=0, column=0, padx=10, pady=10)
        self.frameMenuFinal.place(relx=0.5, rely=0.9, anchor="center")

        self.lienzoLibro = tk.Canvas(master=self.marcoLibros,width=200, height=300)
        self.lienzoLibro.grid(row=0, column=0, padx=10, pady=10)
        self.tituloLibro = CTkLabel(master=self.marcoLibros, text="")
        self.tituloLibro.grid(row=1, column=0, padx=5, pady=5)

        self.ventana.mainloop()

    
    #--------------------FUNCIONES---------------------------------------------------------
    
    def guardarInfo(self):
        titulo = self.entradaTitulo.get()
        autor = self.entradaAutor.get()

        # Si no se carga imagen carga una por defecto
        if self.imagenPath.get() == "":
            rutaImagenPorDefecto = 'img/portadaPorDefecto.png'
            self.imagenPath.set(rutaImagenPorDefecto)
            
            # return

        # Leer la imagen seleccionada
        with open(self.imagenPath.get(), 'rb') as f:
            datosImagen = f.read()

        self.controlador.guardarInfo(titulo, autor, datosImagen)
        self.limpiarCampos()

    # Función para abrir un explorador de archivos y seleccionar una imagen
    def abrirExplorador(self):
        rutaImagen = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccionar imagen", filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png")])
        if rutaImagen:
            self.imagenPath.set(rutaImagen)

    # Función para limpiar los campos de entrada
    def limpiarCampos(self):
        self.entradaTitulo.delete(0, END)
        self.entradaAutor.delete(0, END)
        self.imagenPath.set("")

    def botonTraerLibroPulsado(self):
        titulo = self.entradaBuscarTitulo.get()
        libro = self.controlador.traerLibro(titulo)

        if libro:
            # Actualizar la etiqueta con el título del libro
            self.tituloLibro.configure(text=libro["titulo"])

            # Obtener la imagen de la portada del libro desde GridFS
            imagenPortada = self.controlador.obtenerPortada(libro["portada"])

            if imagenPortada:
                # Mostrar la imagen en el lienzo
                self.mostrarImagenPortada(imagenPortada)
            else:
                print("No se ha obtenido la imagen del libro")
        else:
            print("Libro no encontrado")

    def mostrarImagenPortada(self, datosImagen):
        # Convertir los datos de la imagen en un objeto PhotoImage
        imagen = tk.PhotoImage(data=datosImagen)

        # Mostrar la imagen en el lienzo
        self.lienzoLibro.create_image(0, 0, anchor=tk.NW, image=imagen)

        # Guardar la referencia a la imagen para evitar que sea eliminada por el recolector de basura
        self.lienzoLibro.imagen = imagen
        