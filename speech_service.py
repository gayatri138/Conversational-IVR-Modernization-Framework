import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("IVR:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("User:", text)
        return text

    except:
        return ""