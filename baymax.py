import pyttsx3  # text to speech -> https://pypi.org/project/pyttsx3/

engine = pyttsx3.init()  # initial func. obj creation


############
# Speech
############
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hi, Baymax here how you doing?")