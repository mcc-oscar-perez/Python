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
            
trasformar_audio_en_texto()
