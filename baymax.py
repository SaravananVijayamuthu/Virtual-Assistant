from imports import *

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
    try:
        Time = datetime.datetime.now().strftime("%H:%M:%S")  # converting to str format
        speak(cfg.CurrT)
        speak(Time)
    except Exception as e:
        print(e)
        speak(cfg.CommonErr)


# time()


############
# Date
############
def date():
    try:
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak(cfg.CurrD)
        speak(date)
        speak(month)
        speak(year)
    except Exception as e:
        print(e)
        speak(cfg.CommonErr)


# date()


############
# Greet
############
def greet():
    try:
        speak(cfg.w)
        time()
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
    except Exception as e:
        print(e)
        speak(cfg.CommonErr)


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
        # speak(cfg.NotRecognize)
        return "None"
    return query


# UserCmd()


############
# Wiki Using WikiPedia Lib here search anything with word Baymax results will come from WikiPedia
############
def Pedia(query):
    try:
        speak(cfg.SearchingPedia)
        query = query.replace(cfg.BaymaxPedia, "")
        res = wikipedia.summary(query, sentences=3)
        print(res)
        speak(res)
    except Exception as e:
        print(e)
        speak(cfg.CommonErr)


############
# Browser
############
def Browser():
    try:
        speak(cfg.Search)
        search = UserCmd().lower()
        wbr_Path = cfg.WbrPath
        url = cfg.WebURL.format(search)
        wbr.open_new_tab(url)
    except Exception as e:
        print(e)
        speak(cfg.CommonErr)


############
# Mail
############
def SendMail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()  # checks connection
    server.login("sarvidigilocker@gmail.com", "digiintern")
    server.sendmail("sarvidigilocker@gmail.com", to, content)
    server.close()


############
# Content Mail
############
def contentMail():
    try:
        speak("Message please")
        content = UserCmd()
        to = cfg.sendTo
        SendMail(to, content)
        speak(cfg.SuccessMail)
    except Exception as e:
        print(e)
        speak(cfg.FailureMail)


############
# System Controls
############
def Logout():
    os.system("shutdown /l")


def ShutDown():
    os.system("shutdown /s")


def Restart():
    os.system("shutdown /r")


############
# System Controls
############
def Songs():
    songs_dir = "D://Music"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))


############
# ScreenShot
############
def ScreenShot():
    img = pyautogui.screenshot()
    img.save("D:\\work\\mini_project\\screenshot.png")

############
# Memory
############
def Remember():
    speak(cfg.WhatToRem)
    data = UserCmd()
    speak("Got it I'll remember it")
    mem = open("data.txt", "w")
    mem.write(data)
    mem.close()


def ReturnRem():
    mem = open("data.txt", "r")
    speak(cfg.WhatIRem + mem.read())



############
"""
Main func.
it'll call greet first Then it'll check for the usr voice in query 
and matches and execute the particular func
"""
############
if __name__ == "__main__":
    # greet()  # only once
    while True:
        query = UserCmd().lower()
        if cfg.BaymaxTime in query:
            time()
        elif cfg.BaymaxDate in query:
            date()
        elif cfg.BaymaxPedia in query:
            Pedia(query)
        elif cfg.BaymaxSearch in query:
            Browser()
        elif cfg.BaymaxEmail in query:
            contentMail()
        elif cfg.SysOut in query:
            Logout()
        elif cfg.SysDown in query:
            ShutDown()
        elif cfg.SysStart in query:
            Restart()
        elif cfg.BaymaxSong in query:
            Songs()
        elif cfg.BaymaxMem in query:
            Remember()
        elif cfg.BaymaxHelp in query:
            ReturnRem()
        elif cfg.BaymaxScreenshot in query:
            ScreenShot()
            speak(cfg.Screenshot)
        elif cfg.BaymaxOff in query:
            speak(cfg.MissYou)
            quit()
