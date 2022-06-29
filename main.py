import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(): #Presentacion
    print('''Buenos dias, ¿que deseas hacer? 
    1)registrar pedido 2)leer pedido 3)finalizar''')
    speak("Buenos dias, ¿que deseas hacer?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.5
        audio = r.listen(source)

        try:
            print("Reconociendo...")
            speak("reconociendo")
            query = r.recognize_google(audio,language="es-spanish")
            print(query)
            speak(query)

        except Exception as e:
            print(e)
            print("No se escucho, repita de nuevo")
            speak("No se escucho, repita de nuevo")
            return "None"
        return query
            

if __name__ == "__main__":
    wishme()
    while True:
        query = take_command().lower()

        if 'registra' in query:
            print("que debo registrar?")
            speak("que debo registrar?")
            pedido = take_command()
            print("Pedido registrado: " + pedido)
            speak("Pedido registrado: " + pedido)
            registro = open('pedido.txt','w')
            registro.write(pedido)
            registro.close()
            print('''¿Que mas deseas hacer? 
                    1)registrar pedido 2)leer pedido 3)finalizar''')
            speak("Que mas deseas hacer?")
            
        
        elif 'leer' in query:
            registro = open('pedido.txt','r')
            speak('el pedido es: ' + registro.read())
            quit()
        
        elif 'finaliza' in query:
            print("Nos vemos")
            speak("Nos vemos")
            quit()
            
        elif 'None' in query:
            take_command()
        else:
            print("termino no encontrado")
            speak("termino no encontrado")
            quit()
            