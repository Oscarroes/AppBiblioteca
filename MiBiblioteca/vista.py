from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
import os

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
        
        # Variables
        self.imagenPath = tk.StringVar()
        self.imagenSalir = Image.open("img/iconoEncendido.ico")


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
                                command=self.abrirVentanaInsertar,
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

        #BOTÓN DE MODIFICAR LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="Modificar libro",
                                # command=self.guardarInfo,
                                text_color="#F6FFF9",
                                height=40,
                                width=210,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=1, padx=10, pady=10)

        #BOTÓN DE ELIMINAR LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="Eliminar libro",
                                # command=self.guardarInfo,
                                text_color="#F6FFF9",
                                height=40,
                                width=210,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=2, padx=10, pady=10)

        #BOTÓN DE BUSQUEDA LIBRO
        self.boton = CTkButton(master=self.frameMenu,
                               text="Búsqueda...",
                                # command=self.guardarInfo,
                                text_color="#F6FFF9",
                                height=40,
                                width=210,
                                font=("Roboto", 18, "bold"),
                                corner_radius=32,
                                fg_color="#75CB92",
                                hover_color="#2E4C39",
                                border_color="#636E67",
                                border_width=3)
        self.boton.grid(row=0, column=3, padx=10, pady=10)

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
                                orientation="horizontal", scrollbar_button_color="#75CB92")
        # self.marcoLibros.grid(row=1, columnspan=4, padx=10, pady=10)
        self.marcoLibros.place(relx=0.5, rely=0.5, anchor="center")

        # self.lienzoLibro = tk.Canvas(master=self.marcoLibros,width=200, height=300)
        # self.lienzoLibro.grid(row=0, column=0, padx=10, pady=10)
        # self.tituloLibro = CTkLabel(master=self.marcoLibros, text="")
        # self.tituloLibro.grid(row=1, column=0, padx=5, pady=5)

        #-------------------------FRAME CON MENU FINAL---------------------------------------

        self.frameMenuFinal = CTkFrame(master=self.ventana, width=925, height=50, fg_color="#F6FFF9", border_color="#636E67", border_width=3)
        # self.frameMenu.grid(row=0, column=0, padx=10, pady=10)
        self.frameMenuFinal.place(relx=0.5, rely=0.9, anchor="center")

        #BOTÓN DE CONSULTAR LIBRO
        # self.boton = CTkButton(master=self.frameMenuFinal,
        #                        text="Consultar libro",
        #                         # command=self.guardarInfo,
        #                         text_color="#F6FFF9",
        #                         height=40,
        #                         width=210,
        #                         font=("Roboto", 18, "bold"),
        #                         corner_radius=32,
        #                         fg_color="#75CB92",
        #                         hover_color="#2E4C39",
        #                         border_color="#636E67",
        #                         border_width=3)
        # self.boton.grid(row=0, column=0, padx=10, pady=10)

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
    
    #--------------------VENTANA INSERTAR LIBRO---------------------------------------------------------
        
    def abrirVentanaInsertar(self):
        
        ventanaInsertar = tk.Toplevel(self.ventana)
        ventanaInsertar.geometry("896x896")
        ventanaInsertar.config(bg="#2E4C39")
        ventanaInsertar.title('Añade un nuevo libro')
        ventanaInsertar.lift()

        def posicionarVentana():
            ventanaInsertar.lift()
        
        def cancelarVentanaInsertar():
            ventanaInsertar.destroy()

        self.frameSeparador = CTkFrame(master=ventanaInsertar, fg_color="#2E4C39", height=10)
        self.frameSeparador.grid(row=0, column=0, padx=10, pady=5)

        #ENTRADA TÍTULO--------------------------------------------------
        self.etiquetaTitulo = CTkLabel(master=ventanaInsertar,
                                       text="Título: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaTitulo.grid(row=1, column=0, padx=10, pady=5)
        self.entradaTitulo = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaTitulo.grid(row=1, column=1, padx=10, pady=5)

        #ENTRADA AUTOR-------------------------------------------------------
        self.etiquetaAutor = CTkLabel(master=ventanaInsertar,
                                       text="Autor: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaAutor.grid(row=2, column=0, padx=10, pady=5)
        self.entradaAutor = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaAutor.grid(row=2, column=1, padx=10, pady=0)

        #ENTRADA GÉNERO-------------------------------------------------------

        self.etiquetaGenero = CTkLabel(master=ventanaInsertar,
                                       text="Género: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaGenero.grid(row=3, column=0, padx=10, pady=5)
        self.entradaGenero = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaGenero.grid(row=3, column=1, padx=10, pady=5)

        #ENTRADA PÁGINAS-------------------------------------------------------

        self.etiquetaPaginas = CTkLabel(master=ventanaInsertar,
                                       text="Número de páginas: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaPaginas.grid(row=4, column=0, padx=10, pady=5)
        self.entradaPaginas = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaPaginas.grid(row=4, column=1, padx=10, pady=5)

        #ENTRADA FECHA DE PUBLICACIÓN-------------------------------------------------------

        self.etiquetaFecha = CTkLabel(master=ventanaInsertar,
                                       text="Fecha de publicación: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaFecha.grid(row=5, column=0, padx=10, pady=5)
        self.entradaFecha = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200,
                                       placeholder_text="DD/MM/AAAA",
                                       placeholder_text_color="#B8B8B8")
        self.entradaFecha.grid(row=5, column=1, padx=10, pady=5)

        #ENTRADA EDITORIAL-------------------------------------------------------

        self.etiquetaEditorial = CTkLabel(master=ventanaInsertar,
                                       text="Editorial: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaEditorial.grid(row=6, column=0, padx=10, pady=5)
        self.entradaEditorial = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaEditorial.grid(row=6, column=1, padx=10, pady=5)

        #ENTRADA ISBN-------------------------------------------------------

        self.etiquetaISBN = CTkLabel(master=ventanaInsertar,
                                       text="ISBN: ",
                                       justify="left",
                                       anchor="w",
                                       width=200,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaISBN.grid(row=7, column=0, padx=10, pady=5)
        self.entradaISBN = CTkEntry(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       width=200)
        self.entradaISBN.grid(row=7, column=1, padx=10, pady=5)

        #ENTRADA PORTADA-------------------------------------------------------

        self.etiquetaPortada = CTkLabel(master=ventanaInsertar,
                                        text="Portada: ",
                                        justify="left",
                                        anchor="w",
                                        width=200,
                                        font=("Roboto", 18, "bold"),
                                        text_color="#F6FFF9")
        self.etiquetaPortada.grid(row=8, column=0, padx=10, pady=5)
        self.entradaPortada = CTkEntry(master=ventanaInsertar,
                                        textvariable=self.imagenPath,
                                        state="readonly",
                                        font=("Roboto", 12, "bold"),
                                        width=200)
        self.entradaPortada.grid(row=8, column=2, padx=10, pady=5)

        #BOTÓN DE EXPLORACIÓN
        self.botonExplorador = CTkButton(master=ventanaInsertar,text="Abrir explorador",
                                        command=lambda: [self.abrirExplorador(),posicionarVentana()],
                                        width=200,
                                        text_color="#F6FFF9",
                                        font=("Roboto", 18, "bold"),
                                        fg_color="#75CB92",
                                        hover_color="#4502A0",
                                        border_color="#636E67",
                                        border_width=3)
        self.botonExplorador.grid(row=8, column=1, padx=10, pady=5)

        #ENTRADA SINOPSIS-------------------------------------------------------

        self.etiquetaSinopsis = CTkLabel(master=ventanaInsertar,
                                       text="Sinopsis: ",
                                       justify="left",
                                       anchor="nw",
                                       width=200,
                                       height=250,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        self.etiquetaSinopsis.grid(row=9, column=0, padx=10, pady=5)
        self.entradaSinopsis = CTkTextbox(master=ventanaInsertar,
                                       font=("Roboto", 12, "bold"),
                                       scrollbar_button_color="#75CB92",
                                       width=430,
                                       height=250)
        self.entradaSinopsis.grid(row=9, column=1, columnspan=2, padx=10, pady=5)

        #BOTÓN AGREGAR------------------------------------------------------------

        self.botonAgregar = CTkButton(master=ventanaInsertar,text="Añadir libro",
                                        command=lambda: [self.guardarInfo(),self.limpiarCampos(),posicionarVentana()],
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#75CB92",
                                        hover_color="#4502A0",
                                        border_color="#636E67",
                                        border_width=3)
        self.botonAgregar.grid(row=10, column=1, padx=10, pady=5)

        #BOTÓN CANCELAR-----------------------------------------------------------

        self.botonCancelar = CTkButton(master=ventanaInsertar,text="Cancelar",
                                        command=cancelarVentanaInsertar,
                                        text_color="#F6FFF9",
                                        height=40,
                                        width=210,
                                        font=("Roboto", 18, "bold"),
                                        corner_radius=32,
                                        fg_color="#75CB92",
                                        hover_color="#4502A0",
                                        border_color="#636E67",
                                        border_width=3)
        self.botonCancelar.grid(row=10, column=2, padx=10, pady=5)

    #--------------------VENTANA VER FICHA LIBRO---------------------------------------------------------
        
    def abrirVentanaVerFicha(self, libro):
        
        ventanaVerFicha = tk.Toplevel(self.ventana)
        ventanaVerFicha.geometry("896x896")
        ventanaVerFicha.config(bg="#2E4C39")
        ventanaVerFicha.title('Ficha del libro')
        ventanaVerFicha.lift()

        # marcoImagen = CTkFrame(master=ventanaVerFicha, fg_color="#2E4C39")
        # marcoImagen.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
        # Obtener la imagen de la portada del libro desde GridFS
        imagenPortada = self.controlador.obtenerPortada(libro["portada"])

        imagen = tk.PhotoImage(data=imagenPortada)

        lienzoPortada = tk.Canvas(master=ventanaVerFicha, width=200, height=310)
        lienzoPortada.create_image(0, 0, anchor=tk.NW, image=imagen)
        lienzoPortada.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

        lienzoPortada.imagen = imagen

        etiquetaTitulo = CTkLabel(master=ventanaVerFicha,
                                       text="Título: " + libro["titulo"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaTitulo.grid(row=0, column=1, padx=10, pady=5)

        etiquetaAutor = CTkLabel(master=ventanaVerFicha,
                                       text="Autor: " + libro["autor"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaAutor.grid(row=1, column=1, padx=10, pady=5)

        etiquetaGenero = CTkLabel(master=ventanaVerFicha,
                                       text="Género: " + libro["genero"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaGenero.grid(row=2, column=1, padx=10, pady=5)

        etiquetaPaginas = CTkLabel(master=ventanaVerFicha,
                                       text="Páginas: " + libro["paginas"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaPaginas.grid(row=3, column=1, padx=10, pady=5)

        etiquetaFecha = CTkLabel(master=ventanaVerFicha,
                                       text="Fecha de publicación: " + libro["fecha de publicacion"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaFecha.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

        etiquetaEditorial = CTkLabel(master=ventanaVerFicha,
                                       text="Editorial: " + libro["editorial"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaEditorial.grid(row=5, column=1, padx=10, pady=5)

        etiquetaISBN = CTkLabel(master=ventanaVerFicha,
                                       text="ISBN: " + libro["isbn"],
                                       justify="left",
                                       anchor="w",
                                       width=400,
                                       font=("Roboto", 18, "bold"),
                                       text_color="#F6FFF9")
        etiquetaISBN.grid(row=6, column=1, padx=10, pady=5)

        marcoSinopsis = CTkScrollableFrame(master=ventanaVerFicha,width=600, height=300, fg_color="#F6FFF9", border_color="#636E67", border_width=3,
                                orientation="horizontal", scrollbar_button_color="#75CB92")
        marcoSinopsis.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        etiquetaSinopsis = CTkLabel(master=marcoSinopsis,
                                       text="Sinopsis: \n \n" + libro["sinopsis"],
                                       justify="left",
                                       anchor="nw",
                                       font=("Roboto", 12, "bold"),
                                       text_color="#000000")
        etiquetaSinopsis.grid(row=0, column=0, padx=10, pady=5)


    #--------------------FUNCIONES---------------------------------------------------------    
    
    def salir(self):
        self.ventana.destroy()

    
    def guardarInfo(self):
        titulo = self.entradaTitulo.get()
        autor = self.entradaAutor.get()
        genero = self.entradaGenero.get()
        paginas = self.entradaPaginas.get()
        fecha = self.entradaFecha.get()
        editorial = self.entradaEditorial.get()
        isbn = self.entradaISBN.get()
        sinopsis = self.entradaSinopsis.get("1.0", END)

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

            # Crear una etiqueta para el título del libro y un botón para ver la ficha
            etiquetaTitulo = CTkLabel(master=self.marcoLibros,
                                        text=libro["titulo"],
                                        font=("Roboto", 12, "bold"))
            etiquetaTitulo.grid(row=1, column=i, padx=5, pady=5)

            botonVerFicha = CTkButton(master=self.marcoLibros,
                                        command= lambda libro=libro: self.abrirVentanaVerFicha(libro),
                                        text="Ver ficha",
                                        text_color="#F6FFF9",
                                        font=("Roboto", 18, "bold"),)
            botonVerFicha.grid(row=2, column=i, padx=5, pady=5)
        


    #CREAR FONDO DE IMAGEN Y LUEGO PONER UN FRAME ENCIMA Y LOS WIDGETS EN EL FRAME ¿FUNCIONA?:
        # fondo = tk.PhotoImage(file="fondoDragon.png")
        # canvas = tk.Canvas(raiz, width=fondo.width(), height=fondo.height())
        # canvas.pack()
        # canvas.create_image(0,0,anchor=tk.NW, image=fondo)

        # usuario = tk.Label(canvas,text="Usuario",anchor="w",justify="left",width=22,font=("Verdana",10),bg="#B4B2B2")
        # canvas.create_window(50, 500, anchor=tk.NW, window=usuario)
        # usuarioEntry = tk.Entry(canvas, width=22,font=("Verdana",10),bg="#E7E9E9")
        # canvas.create_window(50, 525, anchor=tk.NW, window=usuarioEntry)
        