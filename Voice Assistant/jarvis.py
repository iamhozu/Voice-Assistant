
from math import e
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import randfacts
from selenium_web import *
from selenium_wiki import *


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
#print(voices[1].id)           
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss")

    else:
        speak("Good Evening Boss")

    speak(" I am Jarvis. Do you need anything Boss?")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1 
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Sorry, Can you say it again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thedemonkinghozaifa@gmail.com', 'whotheh311')
    server.sendmail('thedemonkinghozaifa@gmail.com', to, content)
    server.close()
        




#main function

    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'sumi' in query:
            speak("Sumi is moti moti moti behen")



#search summary of 2 lines on wikipedia
        elif 'wikipedia' in query:
            speak("Searching in Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

#wikipedia search on web page
        elif 'search' in query:
            speak("what do you want to search?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source)
                sec = r.recognize_google(audio)
            speak("Searching {} on Wikipedia".format(sec))
            b = infow()
            b.get_info(sec) 
                  
#youtube video will play but it has some errors
        elif 'play video' in query:
            speak("which video?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source)
                vid = r.recognize_google(audio)
            speak("Playing {} on youtube".format(vid))
            a = youtube()
            a.play(vid)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening Facebook")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening Stack overflow")

        elif 'open open sea' in query:
            webbrowser.open("opensea.io")
            speak("opening open sea NFT market")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hozaifa\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[5]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss the time is{strTime}")

        elif 'open visual code' in query:
            VsPath = 'D:\\Microsoft VS Code\\Code.exe'
            os.startfile(VsPath)

        
        elif 'open photoshop' in query:
            PsPath = 'C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe'
            os.startfile(PsPath)  

        elif 'open video editor' in query:
            PpPath = 'C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2018\\Adobe Premiere Pro.exe'
            os.startfile(PpPath)

        elif 'send a mail to goku' in query:
            try:
                speak('What is the content')
                content = takeCommand()
                to = "hozaifaalam26@gmail.com"
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry Boss, Email was not sent successfully")

        elif 'send mail' in query:
            try:
                speak('What is the content')
                content = takeCommand()
                to = "shahi.kingkai@gmail.com"
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry Boss, Email was not sent successfully")        

#loop error 
#        elif 'fact' or 'facts' in query:
#            x = randfacts.get_fact()
#            print(x)
#            speak("Do you know that ," + x)

                    


        elif 'how are you' in query:
            speak("I am fucking amazing Boss. Dont worry about me.")



        elif 'shutdown' in query:
            sys.exit()
                    





