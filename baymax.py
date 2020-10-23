import pyttsx3  # text to speech
import datetime
import speech_recognition as spr

engine = pyttsx3.init()  # initial func. obj creation


############
# Speech
############
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# speak("Hi, Baymax here how you doing?")


############
# Time
############
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")  # converting to str format
    speak(Time)


# time()


############
# Date
############
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


# date()


############
# Greet
############
def greet():
    speak("Welcome back!")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Hey,Good Morning. Have a nice day!")
    elif hour >= 12 and hour < 18:
        speak("Hey, Good Afternoon. Have a Healthy meal!")
    elif hour >= 18 and hour < 24:
        speak("Hey, Good Evening. Don't forget to go for a walk")
    else:
        speak("Good Night, Sweet dreams")
    speak("Hi I'm Baymax your virtual partner, How can I help you?")


greet()
