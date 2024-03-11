from customtkinter import *
import tkinter as tk
from tkinter import filedialog
import os

class Vista:


    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = CTk()
        self.ventana.geometry("500x400")
        
        # Variables
        # global imagenPath = tk.StringVar()
        self.imagenPath = tk.StringVar()

        self.etiquetaTitulo = CTkLabel(master=self.ventana,text="Titulo")
        self.etiquetaTitulo.pack()
        self.entradaTitulo = CTkEntry(master=self.ventana)
        self.entradaTitulo.pack()

        self.etiquetaAutor = CTkLabel(master=self.ventana,text="Autor")
        self.etiquetaAutor.pack()
        self.entradaAutor = CTkEntry(master=self.ventana)
        self.entradaAutor.pack()

        self.etiquetaPortada = CTkLabel(master=self.ventana,text="Portada")
        self.etiquetaPortada.pack()
        self.entradaPortada = CTkEntry(master=self.ventana, textvariable=self.imagenPath, state="readonly")
        self.entradaPortada.pack()

        self.boton = CTkButton(master=self.ventana,text="Guardar info", command=self.guardarInfo)
        self.boton.place(relx=0.2, rely=0.3, anchor="center")

        self.botonExplorador = CTkButton(master=self.ventana,text="Abrir explorador", command=self.abrirExplorador)
        self.botonExplorador.place(relx=0.8, rely=0.3, anchor="center")

        self.btn = CTkButton(master=self.ventana, text="Traer info", corner_radius=32, fg_color="#C850C0",
           hover_color="#4158D0", border_color="#FFCC70", border_width=2, command=self.controlador.botonPresionado)

        # Centar el botón
        self.btn.place(relx=0.5, rely=0.5, anchor="center")

        self.ventana.mainloop()
    
    def guardarInfo(self):
        titulo = self.entradaTitulo.get()
        autor = self.entradaAutor.get()

        # Si no se carga imagen carga una por defecto
        # if imagenPath.get() == "":
            
        #     return

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
        