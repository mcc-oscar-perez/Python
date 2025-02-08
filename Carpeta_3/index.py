# Index

mi_texto = "Esta es una prueba"
resultado = mi_texto[-1]
print(resultado) 

mi_texto = "Esta es una prueba" 
resultado = mi_texto.index("a", 5, 11) # el primer parametro es el caracter a buscar, el segundo es el inicio de la busqueda y el tercero es el fin de la busqueda
print(resultado)

mi_texto = "Esta es una prueba" 
resultado = mi_texto.rindex("a", 5, 11) # aqi usamos rindex para buscar el caracter de derecha a izquierda
print(resultado)


