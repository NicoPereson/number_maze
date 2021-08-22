import tkinter as tk
from tkinter import ttk
import random

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Laberinto")
        self.salida=False
        self.generar_laberinto()
        self.boton1=ttk.Button(self.ventana1, text="Recorrer", command=self.analizar)
        self.boton1.grid(column=0, row=10, columnspan=5, padx=10, pady=10)
        self.boton2=ttk.Button(self.ventana1, text="Generar otro", command=self.generar_otro)
        self.boton2.grid(column=5, row=10, columnspan=5, padx=10, pady=10)
        self.ventana1.mainloop()

    def generar_laberinto(self):        
        self.tablero = [] #lista que va a guardar el resto de las listas
        listafila = [] #lista vacia que lleno con los label
        for fila in range(0,10):
            for columna in range(0,10):
                label=ttk.Label(self.ventana1, text=self.retornar_aleatorio(), foreground="black")
                label.grid(column=columna, row=fila, padx=10, pady=10) 
                listafila.append(label) 
            self.tablero.append(listafila) 
            listafila = [] 
        self.tablero[0][0].configure(text=0) #configuración de la entrada
        self.tablero[9][9].configure(text=5) #configuración de la salida.

    def generar_otro(self):
        for fila in range(0,10):
            for columna in range(0,10):
                self.tablero[fila][columna].configure(text=self.retornar_aleatorio(),background="#f0f0f0")
        self.tablero[0][0].configure(text=0)
        self.tablero[9][9].configure(text=5)

    def retornar_aleatorio(self):
        valor=random.randint(1,4)
        if valor==1:
            return 1
        else:
            return 0

    def analizar(self):
        self.salida=False
        self.recorrer(0,0)
        if self.salida: #Controlo el resultado del juego
            self.ventana1.title("Tiene salida el laberinto")
        else:
            self.ventana1.title("No tiene salida el laberinto")

    def recorrer(self, fila, columna):
        #Controlo que la coordenada pasada por parámetro (fila, columna) esté dentro del tablero.
        #Controlo que no haya encontrado la salida.
        if fila>=0 and fila<10 and columna>=0 and columna<10 and self.salida==False:
            #Controlo si la cordenada pasada por parámetro es la salida
            if self.tablero[fila][columna].cget("text")==5:
                self.salida=True #Si lo es, pone la bandera en True
            else: 
                #Controlo si la coordenada pasada por parámetro es un pasillo
                if self.tablero[fila][columna].cget("text")==0:
                    #Si es un pasillo, cambio el valor de 0 por 9 para indicar el paso de la persona
                    self.tablero[fila][columna].configure(text=9)
                    #Marco el fondo del label con amarillo para resaltarlo
                    self.tablero[fila][columna].configure(background="yellow")
                    #Muevo a la persona por los cuatro caminos posibles.
                    self.recorrer(fila, columna+1)
                    self.recorrer(fila+1, columna)
                    self.recorrer(fila-1, columna)
                    self.recorrer(fila, columna-1)                        
        
laberinto = Aplicacion()