import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os, serial

recognizer = sr.Recognizer()
mic = sr.Microphone()

port = serial.Serial("COM1",9600)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('voice', 'tr')
    engine.say(text)
    engine.runAndWait()

def listening():
    with mic as m:
        audio = recognizer.listen(m,phrase_time_limit=3)
        
    try:
        text = recognizer.recognize_google(audio,language="tr-TR").lower()
    except:
        text = "anlamadım"
    return text

while True:
    ses = listening()
    print(ses)
    port.write("1".encode())

    if "merhaba" in ses:
        speak("Merhaba")

    elif ("yak" in ses):
        port.write("yak".encode())
        speak("Led yakıldı.")

    elif ("kapat" in ses):
        port.write("kapat".encode())
        speak("Led Kapatıldı.")


    elif "çık" in ses:
        speak("tamam çıkış yapılıyor")
        port.close()
        break

    else:
        speak("anlayamadım")