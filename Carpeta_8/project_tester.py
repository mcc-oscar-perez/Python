"""Auqui provamos el codigo del proyecto"""

#Importamos el modulo necesario
import Proyecto_carpeta_8

def preguntar():
    """Funcion encargada de darle al usuario la opcion que desea seleccionar""" 
    print("Bienvenido a farmacia Python")
    
    while True:
        print("[P] - Perfumeria\n [F] - Farmacia\n [C] - Cosmetica\n")
        try:
            mi_catergoria = input("Elije tu categoria: ").upper()
            ["P","F","C"].index(mi_catergoria)
        except:
            print("Esa no es una opcion valida")
        else:
            break
    
    Proyecto_carpeta_8.decorador(mi_catergoria)

def inicio():
    
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres sacar otro turno? [S] [N]:").upper()
            ["S", "N"].index(otro_turno)
        except:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()