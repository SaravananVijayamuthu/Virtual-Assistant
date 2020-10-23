import pyttsx3  # text to speech -> https://pypi.org/project/pyttsx3/
import datetime

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
