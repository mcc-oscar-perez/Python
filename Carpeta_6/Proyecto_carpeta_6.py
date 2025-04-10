#%%
# Hacer un programa que permita administrar recetas de cocina.
# El programa debe permitir crear recetas, leer recetas, eliminar recetas y crear categorias.
# Las recetas se guardaran en archivos de texto y las categorias seran carpetas.
# Selecciona 1 para leer una receta 
# Selecciona 2 para crar una receta nueva
# Selecciona 3 para crar una categoria nueva 
# Selecciona 4 para eliminar recetas
# Selecciona 5 para eliminar categoria

# Do a project that allows you to manage cooking recipes.
# The program should allow you to create recipes, read recipes, delete recipes and create categories. 
# The recipes will be saved in text files and the categories will be folders.
# Select 1 to read a recipe
# Select 2 to create a new recipe
# Select 3 to create a new category
# Select 4 to delete recipes
# Select 5 to delete category

''' importar modulos ''' 

import os
from os import system 
from pathlib import Path

'''Guardamos la ruta y la cantidad de archivos por carpeta'''

mi_ruta = Path("D:\\Cursos\\PYTHON\\Carpeta_6\\Recetas")

def contar_recetas(ruta):
    contador = 0 
    for i in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


'''Mostrar el menu''' 

def inicio ():
    system("cls")
    print("*" * 40)
    print(" Bienvenido al administrador de recetas")
    print("*" * 40)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")
    
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range (1,7):
        print("Elige una opcion:")
        print('''
              
              [1] - Leer receta
              [2] - Crear receta nueva
              [3] - Crear categoria nueva
              [4] - Eliminar receta
              [5] - Eliminar Categoria 
              [6] - Salir del programa              
              
              ''')
        eleccion = input()
    return int(eleccion)


'''Mostar categorias'''

def mostrar_categorias (ruta):
    
    print("Categorias:")
    lista_categorias = []
    contador2 = 1
    
    for carpeta in ruta.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"{contador2} - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador2 += 1 
    
    return lista_categorias


'''Categoria seleccionada'''

def elegir_categoria (lista):
    eleccion_correcta = 'x'
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\n Elije una categoria:")
        
    return lista[int(eleccion_correcta) - 1]


'''Mostrar recetas'''

def mostrar_recetas (ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador3 = 1
    
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador3}] - {receta_str}")
        lista_recetas.append(receta)
        contador3 += 1 
    return lista_recetas

'''Elegir recetas'''

def elegir_recetas(lista):
    eleccion_receta = 'x'
    
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\n Elije una receta:")
    
    return lista[int(eleccion_receta) - 1]

'''Leer receta'''

def leer_receta(receta):
    print(Path.read_text(receta))

'''Crear receta'''

def crear_receta(ruta):
    existe = False
    
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento esa receta ya existe")

'''Crear categoria'''

def crear_categoria(ruta):
    existe = False
    
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento esa categoria ya existe")

'''Eliminar una receta'''

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"Lara receta {receta.name} ha sido eliminada")

'''Eliminar una categoria'''

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"la categoria {categoria.name} ha sido eliminada")

'''Volver al inicio'''

def volver_inicio():
    eleccion_regresar = 'x'
    
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\n presicone 'v' para volver al menu: ")


Finalizar_programa = False

while not Finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta) 
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        LeerReceta = leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta) 
        mi_categoria = elegir_categoria(mis_categorias)
        CrearReceta = crear_receta(mi_categoria) 
        volver_inicio()

    elif menu == 3: 
        CrearCategoria = crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4: 
        mis_categorias = mostrar_categorias(mi_ruta) 
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminarReceta = eliminar_receta(mi_receta)
        volver_inicio() 

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta) 
        mi_categoria = elegir_categoria(mis_categorias)
        ElimarCategoria = eliminar_categoria(mi_categoria) 
        volver_inicio() 

    elif menu == 6: 
        Finalizar_programa = True
