#Librerias para asistente
import pyttsx3 # sistema que se encarga de hablar con nosotros 
import speech_recognition as sr # Reconoce la voz 
import pywhatkit # permite que el sistema pueda abrir sitios web
import yfinance as yf# revisar la bolsa para revisar acciones 
import pyjokes # para chistes
import webbrowser # manejar navegador de internet
import datetime # fecha 
import wikipedia
import pyaudio


# Escuchar nuestro microfono y devolver el audio como texto

def trasformar_audio_en_texto():
    
    #almacenar recognizer en una variabel
    r = sr.Recognizer()
    
    #configuarar el microfono
    with sr.Microphone() as origen:
    
        #tiempo de espera 
        r.pause_threshold = 0.8 # menos de un segundo 
        
        # informar que comenzo la grabacion 
        print("Ya puedes hablar")
        
        #Guardar lo que esuche como audio
        audio = r.listen(origen)
        
        try:
            # buscar en google lo que haya esuchado
            pedido = r.recognize_google(audio, language="es-MX")
            
            # Prueba de que pudo ingresar 
            print("Dijiste: " + pedido)
            
            # Devolver pedido 
            return pedido
        
        # En caso de no comprender el audio 
        except sr.UnknownValueError:
            
            # Prueba de que no comprendio el audio
            print("Ups, no entendi")
            
            # Devolver error
            return "Sigo esperando"
        
        except sr.RequestError:
            
            # Prueba de que no comprendio el audio
            print("Ups, no hay servicio")
            
            # Devolver error
            return "Sigo esperando"
        
        # Error inesperado
        
        except: 
            
            # Prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")
            
            # Devolver error
            return "Sigo esperando"
            
# funcion para esuchar al asistente 

def hablar(mensaje):
    
    # Encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id_1)
    
    # Pronunciar el mensaje 
    engine.say(mensaje)
    engine.runAndWait()

# Opciones de voz y idioma 
# engine =pyttsx3.init()
# for i in engine.getProperty('voices'):
#     print(i)
    
id_1 ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id_2 ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id_3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# Informacion de la semana 
def pedir_dia():
    
    # Crear variable con datos actualizados 
    dia = datetime.date.today()
    print(dia)
    
    # Crar una variable para el dia de la semanan 
    dia_semana = dia.weekday()
    print(dia_semana)
    
    # Diccionario con los nombres de los dias 
    calendario = {
                0:"Lunes",
                1:"Martes",
                2:"Miércoles",
                3:"Jueves",
                4:"Viernes", 
                5:"Sábado",
                6:"Domingo"
                }
    
    # Decir el dia de la semana 
    hablar(f"Hoy es {calendario[dia_semana]}")

# Informar hora
def pedir_hora():
    
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las, {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)
    
    # Decir la hora
    hablar(hora)

# Saludo inicial 
def Saludo_inicial ():
    
    # Crear variable con datos de hora 
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento = "Buenos días"
    else :
        momento = "Buenas tardes"
    # Decir el saludo 
    hablar(f"¡Hola!, {momento}, soy Miku, tú asistente personal. Por favor, dime en que te puedo ayudar hoy Kevin" )

# Funcion central del asistente 

def pedir_cosas():
    
    #activar el saludo inicial 
    Saludo_inicial()
    
    # Variable de corte 
    comenzar = True
    
    # loop central
    while comenzar:
        
        #activar el microfono 
        pedido = trasformar_audio_en_texto().lower()
        
        if 'abrir youtube' in pedido:
            hablar('Con gusto, abrire  YouTube')
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir navegador'in pedido :
            hablar("Claro, abriendo el buscador web")
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            pedido = pedido.replace("busca en wikipedia", " ")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar("wikipedia dice lo siguiente:")
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            pedido = pedido.replace("busca en internet", " ")
            hablar("con gusto buscare eso por ti")
            pywhatkit.search(pedido)
            hablar("esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            hablar("Excelente buscare ese video")
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma'in pedido:
            hablar(f"muy bien kevin, aqui te va un chiste {pyjokes.get_joke("es")}")
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].split()
            cartera = {
                    'apple':'APPL',
                    'amazon':'AMZN',
                    'google': 'GOOGL'
                    }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f"La encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdona, pero no logre encontrar esa información")   
                continue
        elif 'adiós' in pedido:
            hablar("Muy bien Kevin, me ire a descanzar, cualquier cosa me avisas")
            break
pedir_cosas()
