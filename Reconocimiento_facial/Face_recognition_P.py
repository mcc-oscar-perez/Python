# cargamos las librerias necesarias
# imprtar "os" nos ayuda a trabjar con el sistema operativo
# la libreria numpy ayuda a trabjar con número cuentas y datos
# la libreria datetime nos ayuda a registrar numeros

from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Creamos una base de datos
# la ruta indicar de que carpeta tomara las fotografías
# dejamos una lista de imagenes vacia que se ejecutara cada que se ejecute el programa
# luego obtenemos los nombres de las fotos
# tomamos todos los nombres de todas las fotos que se encuentren en la carpta de alumnos "lista de alumnos"

ruta = 'Alumnos'
mis_imagenes = []
nombres_alumnos = []
lista_alumnos = os.listdir(ruta)

# crearemos un loop for que por cada "nombre dentro de la lista de alumnos"
# declaramos una variable interna "llamada imagen acutla"
# usamos el metodo "imread" para leer la imagen el cual nos pide el nomre de la imagen a leer
# declaramos con una cadena literal que de la caprtea elzada a la variable ruta buscaremos el nombre
# atravez del metodo "append" agregamos la imagen actual en cada loop
# luego agreamos el nombre de los alumnos de nuevo usando "append"
# hacemos que el codigo busque con en la pc con ayuda de la libreria os solicitando que tome el texto de
# cada imagen para dividirlo en indíces y solo tamaremos el indíce cero
# en genral con el loop cargamos la liste de imagenes y nombres

for nombre in lista_alumnos:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_alumnos.append(os.path.splitext(nombre)[0])


print(nombres_alumnos)


# codifcaremos las imagenes
# declaramos una funcion "def"

def codificar (imagenes):

    # crear una lista nueava
    lista_codificada = []

    # pasar todas las imagenes a RGB con ayuda de un loop
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificamos las caras

        codificado = fr.face_encodings(imagen)[0]

        # agreamos a la lista
        lista_codificada.append(codificado)

    # devolver lusta dodificada
    return lista_codificada


# registrar los ingresos
# creamos un archivo llamado "f"
# le pedimos que abra el arhivo almacenado en la carpeta
# "r+" es el formato que le damos al archivo para tener la posivilidad de escribir en el
# cramos una variable llamada lista de datos que nos permitira almacenar y leer todas las líneas
# creamos una lista vacia donde se iran almacenadno las personas que se van registrando en nuestra base

def registrar_ingresos(persona):
    f = open('Registro.csv','r+')
    lista_datos = f.readlines()
    nombres_registro = []

    # ahora por cada línea en la lista de datos
    # cramos una varoanle ingreso que con el metodo "split" nos permite separar donde encuentre una coma
    # hermos que nombres_registro se encargue de almacenar con el metodo appen en la lista,
    # lo que hay en ingresos en su indíce cero

    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

        # si la persona no está en nombres_reguistro
        # cremos una variable que detectara la hora con el metodo "now"
        # luego trasnformamos esa información en un string
        # cremos el formato de mostrar la hora donde %H = hora %M = minutos %S = segundos
        # llamos al archivo con "f" y agreamos el metodo "writelines" para escribir las líneas

        if persona not in nombres_registro:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S')
            f.writelines(f'\n{persona}, {string_ahora}')




# llamamos a la funcion que nos dio en forma de lista peró para llamar a la lista tenemos que
# hacer una varianle para poder almacenar ahi la lista

lista_alumnos_codificada = codificar(mis_imagenes)


# tomar una imagen de camara web el cero es in número de ID
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# leer la imagen de la camara
# declaramos la variable exito en relacion con la variable imagen

exito, imagen = captura.read()

# aqui decimos que si la fotografia no fue exitosa imprimamos eso
# ahora si la foto es exitosa continuamos con el reconmocimiento

if not exito:
    print("No se ah podido tomar la captura")
else:
    #reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coincidencias con un loop pues pasaremos por todas las imagenes de la base de datos
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_alumnos_codificada, caracodif)
        distancias = fr.face_distance(lista_alumnos_codificada, caracodif)

        print(distancias)

        # aqui creamos una variable
        # luego usamos numpy porque trabajermos con datos numericos
        # seleccionamos el metodo "argmin" que lo que hace es reconocre el número más pequeño

        indice_coicidencia = numpy.argmin(distancias)

        #mostrar coincidenicas si las hay
        if distancias[indice_coicidencia] > 0.6:
            print("No coincide con ninngun alumno")

        else:

            #buscar el nombr del alumno encontrado
            nombre = nombres_alumnos[indice_coicidencia]

            # le damos una variable a los cuatro puntos que se generan para dimencionar un rostro
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2),(0,255,0), 2)
            cv2.rectangle(imagen, (x1, y2 -35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)

            # Registramos en el archivo csv a las personas detectadas

            registrar_ingresos(nombre)

            # mostrar la imagen obtenida usando la libreria CV2 que nos ayuda a mostrar cosas
            cv2.imshow('imagen web', imagen)

            # manterner ventada abierta
            cv2.waitKey(0)