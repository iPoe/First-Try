import tkinter
import math
import random
import time

def Menuoperaciones():
    """
    """
    print(" ====================")
    print(" MI PROPIO MP3 PLAYER")
    print(" ====================")
    print("1)Mostrar la lista de canciones")
    print("2)Agregar Canción")
    print("3)Borrar Canción")
    print("4)Reproducir Canción")
    print("5)Finalizar")
    op=0

    while(op <= 1 or op>=5):
            op= eval(input("Ingrese una opcion: "))
                     
            if(op >= 1 and op <=5):
                
                if(op == 1):
                    MostrarListaCanciones(Listacanciones,Listaduraciones)
                if(op == 2):
                    nombre=str(input("Name Song? "))
                    duracion= int(input("Duration? "))
                    Agregarcancion(nombre,duracion,Listacanciones,Listaduraciones)
                    Menuoperaciones()
                if(op == 3):
                    print(str(Listacanciones))                
                    posicion = int(input("What song u want to delete.? "))
                    Borrarcancion(posicion, Listacanciones, Listaduraciones)
                    Menuoperaciones()                
                if(op == 4):
                    print(str(Listacanciones))                
                    posicion=int(input("What song u want to play.? "))
                    Reproducircancion(posicion, Listacanciones, Listaduraciones)
                    Menuoperaciones()
                if(op == 5):
                    exit()













                    

