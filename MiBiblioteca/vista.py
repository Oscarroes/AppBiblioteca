from customtkinter import *
import customtkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
import os

from vistaFicha import VistaFicha
from vistaInsertar import VistaInsertar

class Vista:


    def __init__(self, controlador):
        self.controlador = controlador

        #----------------------------INTERFAZ GRÁFICA-----------------------------------------

        self.ventana = CTk()
        self.ventana.geometry("1024x640")
        self.ventana.resizable(False, False)
        self.ventana.configure(fg_color="#2E4C39")
        self.ventana.title('Mi Biblioteca')
        self.ventana.iconbitmap('img/iconoLibros.ico')

        # Inicialización de las VISTAS secundarias:
        self.llamarVistaInsertar = VistaInsertar(self.ventana, self.controlador, self)
        self.llamarVistaFicha = VistaFicha(self.ventana, self.controlador, self)
        
        
        # Variables
        self.imagenPath = tk.StringVar()
        self.imagenSalir = Image.open("img/iconoEncendido.ico")

        #-----------------------FRAME CON MENU INICIAL-------------------------------------

        self.frameMenu = CTkFrame(master=self.ventana, width=925, height=50, fg_color="#F6FFF9", border_color="#636E67", border_width=3)
        # self.frameMenu.grid(row=0, column=0, padx=10, pady=10)
        self.frameMenu.place(relx=0.5, rely=0.1, anchor="center")

        #BOTÓN DE AGREGAR NUEVO LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="Nuevo libro",
                                # command=self.abrirVentanaInsertar,
                                command=self.llamarVistaInsertar.abrirVentanaInsertar,
                                text_color="#F6FFF9",
                                height=40,
                                width=190,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=0, padx=10, pady=10)

        #BOTÓN DE PRUEBA 1 LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="placeHolder libro",
                                # command=self.guardarInfo,
                                text_color="#F6FFF9",
                                height=40,
                                width=190,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=1, padx=10, pady=10)

        #BOTÓN DE PRUEBA 2 LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="placeHolder libro",
                                # command=self.guardarInfo,
                                text_color="#F6FFF9",
                                height=40,
                                width=190,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=2, padx=10, pady=10)

        #COMBOBOX DE BUSQUEDA LIBRO
        self.comboBox = customtkinter.CTkOptionMenu(master=self.frameMenu,
                                values=["Busca por título", "Busca por autor", "Busca por género"],
                                command=self.menuOpciones,
                                text_color="#F6FFF9",
                                height=40,
                                width=260,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                button_color="#2E4C39",
                                dropdown_fg_color="#75CB92",
                                dropdown_font=("Roboto", 18, "bold"),
                                dropdown_text_color="#F6FFF9",
                                dropdown_hover_color="#2E4C39"
                                )
        self.comboBox.grid(row=0, column=3, padx=10, pady=10)

        #-------------------------FRAME CON SCROLLBAR---------------------------------------------

        self.marcoLibros = CTkScrollableFrame(master=self.ventana,width=900, height=400, fg_color="#F6FFF9", border_color="#636E67", border_width=3,
                                orientation="horizontal", scrollbar_button_color="#75CB92")
        # self.marcoLibros.grid(row=1, columnspan=4, padx=10, pady=10)
        self.marcoLibros.place(relx=0.5, rely=0.5, anchor="center")

        #-------------------------FRAME CON MENU FINAL---------------------------------------

        self.frameMenuFinal = CTkFrame(master=self.ventana, width=925, height=50, fg_color="#F6FFF9", border_color="#636E67", border_width=3)
        # self.frameMenu.grid(row=0, column=0, padx=10, pady=10)
        self.frameMenuFinal.place(relx=0.5, rely=0.9, anchor="center")

        #BOTÓN DE MIBIBLIOTECA
        self.boton = CTkButton(master=self.frameMenuFinal,
                               text="Mi biblioteca",
                                command=self.mostrarLibros,
                                text_color="#F6FFF9",
                                height=40,
                                width=210,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=0, padx=10, pady=10)

        #BOTÓN DE SALIR
        self.boton = CTkButton(master=self.frameMenuFinal,
                                text="Salir",
                                command=self.salir,
                                text_color="#F6FFF9",
                                height=40,
                                width=210,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                image=CTkImage(light_image=self.imagenSalir),
                                fg_color="#ef404c",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=1, columnspan=3, padx=240, pady=10)

        self.ventana.mainloop()

    #--------------------VENTANA BUSCAR POR TITULO---------------------------------------------------------
    def abrirVentanaTitulo(self):
        VentanaTitulo = tk.Toplevel(self.ventana)
        VentanaTitulo.geometry("448x320")
        VentanaTitulo.config(bg="#2E4C39")
        VentanaTitulo.title('Búsqueda por título')
        VentanaTitulo.lift()

        self.etiquetaTitulo = CTkLabel(master=VentanaTitulo,
                                       text="Título: ",
                                       justify="left",
                                       anchor="w",
                                       width=100,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaTitulo.grid(row=1, column=0, padx=10, pady=20)

        self.entradaTitulo = CTkEntry(master=VentanaTitulo,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaTitulo.grid(row=1, column=1, padx=10, pady=20)

        self.botonBuscarPorTitulo = CTkButton(master=VentanaTitulo,
                                        text="Buscar libro",
                                        command=self.buscarLibroPorTitulo,
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#75CB92",
                                        hover_color="#4502A0",
                                        border_color="#636E67",
                                        border_width=3)
        self.botonBuscarPorTitulo.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

    #--------------------VENTANA BUSCAR POR AUTOR---------------------------------------------------------
    def abrirVentanaAutor(self):
        VentanaAutor = tk.Toplevel(self.ventana)
        VentanaAutor.geometry("448x320")
        VentanaAutor.config(bg="#2E4C39")
        VentanaAutor.title('Búsqueda por autor')
        VentanaAutor.lift()

        self.etiquetaAutor = CTkLabel(master=VentanaAutor,
                                       text="Autor: ",
                                       justify="left",
                                       anchor="w",
                                       width=100,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaAutor.grid(row=1, column=0, padx=10, pady=20)

        self.entradaAutor = CTkEntry(master=VentanaAutor,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaAutor.grid(row=1, column=1, padx=10, pady=20)

        self.botonBuscarPorAutor = CTkButton(master=VentanaAutor,
                                        text="Buscar libro",
                                        command=self.buscarLibroPorAutor,
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#75CB92",
                                        hover_color="#4502A0",
                                        border_color="#636E67",
                                        border_width=3)
        self.botonBuscarPorAutor.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

    #--------------------VENTANA BUSCAR POR GENERO---------------------------------------------------------
    def abrirVentanaGenero(self):
        VentanaGenero = tk.Toplevel(self.ventana)
        VentanaGenero.geometry("448x320")
        VentanaGenero.config(bg="#2E4C39")
        VentanaGenero.title('Búsqueda por género')
        VentanaGenero.lift()

        self.etiquetaGenero = CTkLabel(master=VentanaGenero,
                                       text="Género: ",
                                       justify="left",
                                       anchor="w",
                                       width=100,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaGenero.grid(row=1, column=0, padx=10, pady=20)

        self.entradaGenero = CTkEntry(master=VentanaGenero,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaGenero.grid(row=1, column=1, padx=10, pady=20)

        self.botonBuscarPorGenero = CTkButton(master=VentanaGenero,
                                        text="Buscar libro",
                                        command=self.buscarLibroPorGenero,
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#75CB92",
                                        hover_color="#4502A0",
                                        border_color="#636E67",
                                        border_width=3)
        self.botonBuscarPorGenero.grid(row=2, column=0, columnspan=2, padx=10, pady=20)


    #--------------------FUNCIONES---------------------------------------------------------    
    
    def salir(self):
        self.ventana.destroy()

    def menuOpciones(self, opcion):
        if opcion == "Busca por título":
            self.abrirVentanaTitulo()
        if opcion == "Busca por autor":
            self.abrirVentanaAutor()
        if opcion == "Busca por género":
            self.abrirVentanaGenero()

    #Función para guardar libro:
    def guardarInfo(self):
        titulo = self.entradaTitulo.get()
        autor = self.entradaAutor.get()
        genero = self.entradaGenero.get()
        paginas = self.entradaPaginas.get()
        fecha = self.entradaFecha.get()
        editorial = self.entradaEditorial.get()
        isbn = self.entradaISBN.get()
        sinopsis = self.entradaSinopsis.get("1.0", END)

        #Si no se introducen valores, cargar valores por defecto
        if self.entradaTitulo.get() == "":
            titulo = "Título no encontrado"
        if self.entradaAutor.get() == "":
            autor = "Autor no encontrado"
        if self.entradaGenero.get() == "":
            genero = "Género no encontrado"
        if self.entradaPaginas.get() == "":
            paginas = "Número de páginas no encontrado"
        if self.entradaFecha.get() == "":
            fecha = "No encontrada"
        if self.entradaEditorial.get() == "":
            editorial = "Editorial no encontrada"
        if self.entradaISBN.get() == "":
            isbn = "Númrero de ISBN no encontrado"
        if self.entradaSinopsis.get("1.0", END) == "":
            sinopsis = "Sinopsis no encontrada"

        # Si no se carga imagen carga una por defecto
        if self.imagenPath.get() == "":
            rutaImagenPorDefecto = 'img/portadaPorDefecto.png'
            self.imagenPath.set(rutaImagenPorDefecto)
            
            # return

        # Leer la imagen seleccionada
        with open(self.imagenPath.get(), 'rb') as f:
            datosImagen = f.read()

        self.controlador.guardarInfo(titulo, autor, genero, paginas, fecha, editorial, isbn, datosImagen, sinopsis)
        self.limpiarCampos()
        messagebox.showinfo("Añadir Libro", "El libro " + titulo +" ha sido añadido a la biblioteca")

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
        self.entradaGenero.delete(0, END)
        self.entradaPaginas.delete(0, END)
        self.entradaFecha.delete(0, END)
        self.entradaEditorial.delete(0, END)
        self.entradaISBN.delete(0, END)
        self.entradaSinopsis.delete("1.0", END)


    #BUSCAR LIBRO POR TITULO --------------------------------------------------------------
    def buscarLibroPorTitulo(self):

        # Limpiar el contenido anterior del marcoLibros
        for widget in self.marcoLibros.winfo_children():
            widget.destroy()
        titulo = self.entradaTitulo.get()
        libros = self.controlador.traerLibro(titulo)

        # Convertir el cursor a una lista para poder verificar si hay algún libro
        libros = list(libros)

        if libros:

            for i, libro in enumerate(libros):
                #Creamos un lienzo para la portada del libro
                lienzoPortada = tk.Canvas(master=self.marcoLibros, width=200, height=310)
                lienzoPortada.grid(row=0, column=i, padx=10, pady=10)

                #Obtenemos la imagen de la portada desde GridFS
                imagenPortada = self.controlador.obtenerPortada(libro["portada"])

                if imagenPortada:
                    # Convertir los datos de la imagen en un objeto PhotoImage
                    imagen = tk.PhotoImage(data=imagenPortada)

                    # Mostrar la imagen en el lienzo
                    lienzoPortada.create_image(0, 0, anchor=tk.NW, image=imagen)

                    # Guardar la referencia a la imagen para evitar que sea eliminada por el recolector de basura
                    lienzoPortada.imagen = imagen

                # Crear una etiqueta para el título del libro y un botón para ver la ficha
                etiquetaTitulo = CTkLabel(master=self.marcoLibros,
                                            text=libro["titulo"],
                                            font=("Roboto", 12, "bold"))
                etiquetaTitulo.grid(row=1, column=i, padx=5, pady=5)

                botonVerFicha = CTkButton(master=self.marcoLibros,
                                            command= lambda libro=libro: self.llamarVistaFicha.abrirVentanaVerFicha(libro),
                                            text="Ver ficha",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),)
                botonVerFicha.grid(row=2, column=i, padx=5, pady=5)

                botonEliminarLibro = CTkButton(master=self.marcoLibros,
                                            command=lambda idLibro=libro["_id"]: self.eliminarLibro(idLibro),
                                            text="Eliminar libro",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),
                                            fg_color="#ef404c",
                                            hover_color="#2E4C39")
                botonEliminarLibro.grid(row=3, column=i, padx=5, pady=5)
        else:
            # Si no se encontraron libros, muestra un mensaje al usuario
            messagebox.showinfo("Búsqueda por título", "No se encontraron libros con ese título")

    #BUSCAR LIBRO POR AUTOR --------------------------------------------------------------
            
    def buscarLibroPorAutor(self):

        # Limpiar el contenido anterior del marcoLibros
        for widget in self.marcoLibros.winfo_children():
            widget.destroy()
        autor = self.entradaAutor.get()
        libros = self.controlador.traerLibroAutor(autor)

        # Convertir el cursor a una lista para poder verificar si hay algún libro
        libros = list(libros)

        if libros:

            for i, libro in enumerate(libros):
                #Creamos un lienzo para la portada del libro
                lienzoPortada = tk.Canvas(master=self.marcoLibros, width=200, height=310)
                lienzoPortada.grid(row=0, column=i, padx=10, pady=10)

                #Obtenemos la imagen de la portada desde GridFS
                imagenPortada = self.controlador.obtenerPortada(libro["portada"])

                if imagenPortada:
                    # Convertir los datos de la imagen en un objeto PhotoImage
                    imagen = tk.PhotoImage(data=imagenPortada)

                    # Mostrar la imagen en el lienzo
                    lienzoPortada.create_image(0, 0, anchor=tk.NW, image=imagen)

                    # Guardar la referencia a la imagen para evitar que sea eliminada por el recolector de basura
                    lienzoPortada.imagen = imagen

                # Crear una etiqueta para el título del libro y un botón para ver la ficha
                etiquetaTitulo = CTkLabel(master=self.marcoLibros,
                                            text=libro["titulo"],
                                            font=("Roboto", 12, "bold"))
                etiquetaTitulo.grid(row=1, column=i, padx=5, pady=5)

                botonVerFicha = CTkButton(master=self.marcoLibros,
                                            command= lambda libro=libro: self.llamarVistaFicha.abrirVentanaVerFicha(libro),
                                            text="Ver ficha",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),)
                botonVerFicha.grid(row=2, column=i, padx=5, pady=5)

                botonEliminarLibro = CTkButton(master=self.marcoLibros,
                                            command=lambda idLibro=libro["_id"]: self.eliminarLibro(idLibro),
                                            text="Eliminar libro",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),
                                            fg_color="#ef404c",
                                            hover_color="#2E4C39")
                botonEliminarLibro.grid(row=3, column=i, padx=5, pady=5)
        else:
            # Si no se encontraron libros, muestra un mensaje al usuario
            messagebox.showinfo("Búsqueda por autor", "No se encontraron libros con ese autor")

    #BUSCAR LIBRO POR GENERO --------------------------------------------------------------
            
    def buscarLibroPorGenero(self):

        # Limpiar el contenido anterior del marcoLibros
        for widget in self.marcoLibros.winfo_children():
            widget.destroy()
        genero = self.entradaGenero.get()
        libros = self.controlador.traerLibroGenero(genero)

        # Convertir el cursor a una lista para poder verificar si hay algún libro
        libros = list(libros)

        if libros:

            for i, libro in enumerate(libros):
                #Creamos un lienzo para la portada del libro
                lienzoPortada = tk.Canvas(master=self.marcoLibros, width=200, height=310)
                lienzoPortada.grid(row=0, column=i, padx=10, pady=10)

                #Obtenemos la imagen de la portada desde GridFS
                imagenPortada = self.controlador.obtenerPortada(libro["portada"])

                if imagenPortada:
                    # Convertir los datos de la imagen en un objeto PhotoImage
                    imagen = tk.PhotoImage(data=imagenPortada)

                    # Mostrar la imagen en el lienzo
                    lienzoPortada.create_image(0, 0, anchor=tk.NW, image=imagen)

                    # Guardar la referencia a la imagen para evitar que sea eliminada por el recolector de basura
                    lienzoPortada.imagen = imagen

                # Crear una etiqueta para el título del libro y un botón para ver la ficha
                etiquetaTitulo = CTkLabel(master=self.marcoLibros,
                                            text=libro["titulo"],
                                            font=("Roboto", 12, "bold"))
                etiquetaTitulo.grid(row=1, column=i, padx=5, pady=5)

                botonVerFicha = CTkButton(master=self.marcoLibros,
                                            command= lambda libro=libro: self.llamarVistaFicha.abrirVentanaVerFicha(libro),
                                            text="Ver ficha",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),)
                botonVerFicha.grid(row=2, column=i, padx=5, pady=5)

                botonEliminarLibro = CTkButton(master=self.marcoLibros,
                                            command=lambda idLibro=libro["_id"]: self.eliminarLibro(idLibro),
                                            text="Eliminar libro",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),
                                            fg_color="#ef404c",
                                            hover_color="#2E4C39")
                botonEliminarLibro.grid(row=3, column=i, padx=5, pady=5)
        else:
            # Si no se encontraron libros, muestra un mensaje al usuario
            messagebox.showinfo("Búsqueda por género", "No se encontraron libros con ese género")

    def mostrarLibros(self):
        libros = self.controlador.consultarTodo()

        for i, libro in enumerate(libros):
            #Creamos un lienzo para la portada del libro
            lienzoPortada = tk.Canvas(master=self.marcoLibros, width=200, height=310)
            lienzoPortada.grid(row=0, column=i, padx=10, pady=10)

            #Obtenemos la imagen de la portada desde GridFS
            imagenPortada = self.controlador.obtenerPortada(libro["portada"])

            if imagenPortada:
                # Convertir los datos de la imagen en un objeto PhotoImage
                imagen = tk.PhotoImage(data=imagenPortada)

                # Mostrar la imagen en el lienzo
                lienzoPortada.create_image(0, 0, anchor=tk.NW, image=imagen)

                # Guardar la referencia a la imagen para evitar que sea eliminada por el recolector de basura
                lienzoPortada.imagen = imagen

            # Crear una etiqueta para el título del libro, un botón para ver la ficha y otro para eliminar el libro
            etiquetaTitulo = CTkLabel(master=self.marcoLibros,
                                        text=libro["titulo"],
                                        font=("Roboto", 12, "bold"))
            etiquetaTitulo.grid(row=1, column=i, padx=5, pady=5)

            botonVerFicha = CTkButton(master=self.marcoLibros,
                                        command= lambda libro=libro: self.llamarVistaFicha.abrirVentanaVerFicha(libro),
                                        text="Ver ficha",
                                        text_color="#F6FFF9",
                                        font=("Roboto", 18, "bold"),)
            botonVerFicha.grid(row=2, column=i, padx=5, pady=5)

            botonEliminarLibro = CTkButton(master=self.marcoLibros,
                                            command=lambda idLibro=libro["_id"]: self.eliminarLibro(idLibro),
                                            text="Eliminar libro",
                                            text_color="#F6FFF9",
                                            font=("Roboto", 18, "bold"),
                                            fg_color="#ef404c",
                                            hover_color="#2E4C39")
            botonEliminarLibro.grid(row=3, column=i, padx=5, pady=5)

    #ELIMINAR LIBRO:
            
    def eliminarLibro(self, idLibro):

        pregunta = messagebox.askyesno("Eliminar libro", "¿Estás seguro de que quieres eliminar este libro?")
        if pregunta:
            self.controlador.eliminarLibro(idLibro)
            messagebox.showinfo("Eliminar libro", "El libro ha sido eliminado correctamente.")

            # Limpiar el contenido anterior del marcoLibros
            self.actualizarMarcoLibros()

    def actualizarMarcoLibros(self):
        # Limpiar el contenido anterior del marcoLibros
        for widget in self.marcoLibros.winfo_children():
            widget.destroy()
            #Actualizar el listado de libros de la biblioteca   
        self.mostrarLibros()
 
        