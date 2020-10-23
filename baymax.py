import datetime

import pyttsx3  # text to speech
import speech_recognition as spr

import config as cfg

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
    speak(cfg.w)
    speak(cfg.CurrT)
    time()
    speak(cfg.CurrD)
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(cfg.Morning)
    elif hour >= 12 and hour < 18:
        speak(cfg.Afternoon)
    elif hour >= 18 and hour < 24:
        speak(cfg.Evening)
    else:
        speak(cfg.Night)
    speak(cfg.Welcome)


# greet()


############
# User Cmd
############
def UserCmd():
    rec = spr.Recognizer()
    with spr.Microphone() as source:  # Getting usr cmd through mic
        print("Listening..")
        rec.pause_threshold = 1  # Waiting time
        audio = rec.listen(source)  # listeen to microphone
    try:
        print("Recognizing..")
        query = rec.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak(cfg.NotRecognize)
        return "None"
    return query


UserCmd()
