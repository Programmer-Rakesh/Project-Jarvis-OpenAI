import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 195)      # Voice speed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "none"
    return query

if __name__=="__main__":
    while True:
        query = takeCommand().lower()
        if 'Hey Jarvis' in query:
            print("Yes sir")
            speak("Yes sir")