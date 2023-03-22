import speech_recognition as sr
import pyttsx3
import transformers
import os
import datetime
import numpy as np
import webbrowser
import psutil
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
print(connect())
if connect:
    class ChatBot():
        def __init__(self, name):
            print("--- starting up", name, "---")
            self.name = name
    
        def speech_to_text(self):
            recognizer = sr.Recognizer()
            with sr.Microphone() as mic:
                self.text=input("You:")
        @staticmethod
        def speak(text):
            print("JUNE--> ", text)
            engine = pyttsx3.init() # object creation
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', voices[1].id)
            rate=engine.getProperty('rate')
            engine.setProperty('rate',170)
            engine.say(text)
            engine.runAndWait()
    
        def wake_up(self, text):
            if self.name in text.lower():
                return True
            else :
                return False
    
        @staticmethod
        def action_time():
            return datetime.datetime.now().time().strftime('%H:%M')
    
    def goToSleep(june):
        while True:
            june.speech_to_text()
            if june.wake_up(june.text) is True:
                june.speak("I'm awake!")
                return None
            else:
                continue
    def ProjectModeAssistant(june):
        while True:
            cmd=june.text
            
    # Run the june
    if __name__ == "__main__":
        
        june = ChatBot(name="june")
        nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-large")
        os.environ["TOKENIZERS_PARALLELISM"] = "true"
        june.speak("JUNE at your service")
        june.speak("Please wait for a few seconds. ")
        june.speak("Importing Battery Status.....")
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        bts=battery.percent
        if(bts<=15 and bts>5 and plugged==False):
            june.speak("Warning! LOW BATTERY! PLEASE PLUGIN")
        elif(bts>=15 and plugged==True):
            june.speak("Charging.......")
        elif(bts<=5 and plugged==False):
                  june.speak('Not enough charge to host me')
                  os.system("shutdown /s /t 1")
        else:
            june.speak("Import complete... battery status ="+str(bts)+"%. You may now command me.")
        while True:
            cmd=june.speech_to_text()
            print(cmd)
            var4 = ['who are you', 'what is your name']
            cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
            cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
            jokes = ['Can a kangaroo jump higher than a house?\n Of course,\n a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot.\n It got so bad, finally I had to take his bike away.', "Why cant a aethist solve exponenetial problems?\n  Because he/she doesn't believe in higher power","what did the proton tell the electron?\n  don't be so negative.",'Reaching the end of a job interview,\n the Human Resources Officer asks a young engineer fresh out of the Massachusetts Institute of Technology,\n "And what starting salary are you looking for?"\n The engineer replies,\n "In the region of $125,000 a year, depending on the benefits package."\m The interviewer inquires,\n "Well, what would you say to a package of five weeks vacation,\n 14 pjuned holidays,\n full medical and dental,\n company matching retirement fund to 50% of salary,\n and a company car leased every two years,\n say, a red Corvette?"\n The engineer sits up strjuneght and says,\n "Wow!\n Are you kidding?" \n The interviewer replies, \n"Yeah, but you started it.']
            cmd4 = ['open youtube', 'i want to watch a video']
            cmd5 = ['tell me the weather', 'weather', 'what about the weather','what is the weather today']
            fav=["play my favourite song"]
            stat=["battery status","check battery status"]
            pmode=["lets get to work","project mode","switch to project mode","lets start working"]
                ## wake up
             res=""
            state="ON"
            print(june.text)
            if june.text in var4:
                res = "Hello I am JUNE. My full name is Just Understanding Neural Electronics. what can I do for you?"
            elif june.wake_up(june.text) and state=="OFF":
                res="Am Awake"
            ## action time
            elif "time" in june.text:
                res = june.action_time()
            ## respond politely
            elif any(i == june.text for i in ["thank","thanks"]):
                res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","peace out!"])
            elif any(i == june.text for i in["goodbye","bye","let's call it a day"]):
                res="Goodbye! Hope to see ya soon"
                state="OFF"
            elif any(i == june.text for i in cmd2):
                res="Playing your favourite music"
                webbrowser.open("open.spotify.com")
            elif any(i == june.text for i in cmd5):
                webbrowser.open("https://www.bing.com/search?q=today%27s+weather+forecast&qs=SC&pq=today%27s+wae&sc=8-11&cvid=529AB3594F30416DB2A557F154BCB435&FORM=GEOTRI&sp=1&ghc=1&isRef=1&showTw=1")
            elif any(i == june.text for i in cmd3):
                res=np.random.choice(jokes)
            elif any(i.lower() == june.text for i in cmd4):
                webbrowser.open("www.youtube.com")
            elif any(i == june.text for i in stat):
                res=str(psutil.sensors_battery())
            elif any(i == june.text for i in pmode):
                ProjectModeAssistant(june)
            ## conversation
            elif june.text=="":
                goToSleep(june)
            else:   
                chat = nlp(transformers.Conversation(june.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()
    
            june.speak(res)
            if state=="OFF":
                break
            else:
                continue