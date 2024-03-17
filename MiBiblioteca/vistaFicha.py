import tkinter as tk
from customtkinter import *
from tkinter import messagebox
import os

class VistaFicha:

    def __init__(self, ventana, controlador):
        self.ventana = ventana
        self.controlador = controlador
        self.ventanaVerFicha = None

    def abrirVentanaVerFicha(self, libro):
            
            ventanaVerFicha = tk.Toplevel(self.ventana)
            ventanaVerFicha.geometry("896x896")
            ventanaVerFicha.config(bg="#2E4C39")
            ventanaVerFicha.title('Ficha del libro')
            ventanaVerFicha.lift()

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
