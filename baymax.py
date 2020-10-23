import pyttsx3  # text to speech -> https://pypi.org/project/pyttsx3/

engine = pyttsx3.init() #initial func. obj creation
engine.say("Hi, Baymax here")
engine.runAndWait()
