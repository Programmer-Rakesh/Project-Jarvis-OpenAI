import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
#engine.say("Hello world")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()    

#speak("This is Jarvis AI assistant")
#speak("The current time is")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")     
    speak(Time)

#time()
#speak("The current date is")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)      #convert int to variable
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
#date()    

def wishme():
    speak('Welcome back sir')
    speak("the current time is")
    time()
    speak("the current dat is")
    date()
    speak("Jarvis at your service. please tell me how may I help you ?")

#wishme()  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("say that again please...")
        return "none"
    return query

takeCommand()    