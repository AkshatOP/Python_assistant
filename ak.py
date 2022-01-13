import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import cv2
import sys
import time
from requests import get
import pywhatkit





brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s' #Change this path to your system browser's path 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Axew, currently operating on you system made by AK. Please say START when you wish to use me")       

def takeCommand():
    try:
        
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(f"User said: {query}\n")
            print("No commands found related to query")  
        
            return "None"
        return query
    except KeyboardInterrupt:
        pass


def takeStartCommand():
    try:
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)

        try:   
            query = r.recognize_google(audio, language='en-in')
        

        except Exception as e:  
            return "None"
        return query
    except KeyboardInterrupt:
        pass


def ToList(string):
    li = list(string.split(" "))
    return li
    
    


if __name__ == "__main__":
    wishMe()
    while True:     
        FrstQuery = takeStartCommand().lower()
        if 'start' in FrstQuery:
            print(f"User Initated Me")
            speak("How May I Help you?")

                
            query = takeCommand().lower()

        # Logic for executing tasks based on query
            if 'wikipedia' in query:
               speak('Searching Wikipedia...')
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query, sentences=2)
               speak("According to Wikipedia")
               print(results)
               speak(results)
#<=====================Commands List=========================================>
            elif 'what you can do' in query:
                speak("Sir I can do many things like opening youtube calculator clock stackoveflow on-screenkeyboard discord and perform different things like google search , youtube search , say the current time , take a photo , show your ip address")
#<=====================Owner Ki tareef hehe=========================================>
            elif 'who made you' in query:
                speak("I was made in the topsecret laboratory run by my master AK")
#<=====================OPENS YOUTUBE=========================================>
            elif 'open youtube' in query:
               webbrowser.get(brave_path).open("youtube.com")
#<======================OPENS COMMAND PROMPT===============================>
            elif 'open command prompt' in query:
               os.system('start cmd')    
#<=======================OPENS GOOGLE======================================>
            elif 'open google' in query:
               webbrowser.get(brave_path).open("google.com")
#<=========OPENS GOOGLE AND SEARCH FOR THE QUERY GIVEN BY USER===========>        
            elif 'google search' in query:
               speak("What should i search on google sir ?")
               cm = takeCommand().lower()
               pywhatkit.search(cm)
               print("Searching...")

#<=========OPENS YOUTUBE AND SEARCH FOR THE QUERY GIVEN BY USER===========>
            elif 'youtube search' in query: 
                speak("What should i search on youtube sir ?")
                cm = takeCommand().lower() 
                print(cm)
                a = "+"
                a = a.join(ToList(cm))
                webbrowser.get(brave_path).open(f"https://www.youtube.com/results?search_query={a}")   
 
#<===================OPENS INTERNAL CAMERA===========================>
            elif 'open camera' in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam, img')
                    k = cv2.waitKey(50)
                    if k==27:
                       break;
                cap.release()
                cv2.destroyAllWindows()    
#<======================OPENS STACK OVERFLOW=========================>               
            elif 'open stackoverflow' in query:
                webbrowser.get(brave_path).open("stackoverflow.com")   
#<=========================SHOWS MY IP ADDRESS=======================>
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                print({ip})
                speak(f"Your IP address is {ip}")
#<=============PLAYS MUSIC FROM THE DIRECTORY INDICATED==============>
            elif 'play music' in query:
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
#<=======================TELLS THE CURRENT TIME=====================>
            elif 'what is the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
#<==========================OPENS VSC================================>
            elif 'open code' in query:
                codePath = "C:\\Users\\AK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
#<==========================OPENS ALARM/CLOCK================================>
            elif 'open clock' in query:
                os.startfile('start explorer shell:appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App') 
#<==========================OPENS CALCULATOR================================>
            elif 'open calculator' in query:
                os.startfile('calc.exe')              
#<==========================OPENS NOTEPAD================================>
            elif 'open notepad' in query:
                os.startfile('notepad.exe')  
#<==========================OPENS ON-SCREEN KEYBOARD================================>
            elif 'open screen keyboard' in query:
                os.startfile('osk.exe')  
#<==========================OPENS ON-SCREEN KEYBOARD================================>
            elif 'open run' in query:
                os.startfile('start explorer shell:appsfolder\Microsoft.Windows.Shell.RunDialog')
#<==========================OPENS DISCORD ===========================>           
            elif 'open discord app' in query:
                codePath = "C:\\Users\\AK\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
                os.startfile(codePath)

            elif 'open discord' in query:
                webbrowser.get(brave_path).open("discord.com/login")

#<==============================Opens ON SCREEN KEYBOARD===========================>
            elif 'open screen keyboard' in query:
                os.startfile("{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\osk.exe")
#<==============================SHUTS OFF AXEW===========================>
            elif 'close your system' in query:
                speak("Ok sir, I am closing my system. Have a good day")       
                sys.exit()

            else:
                speak("Sorry I didn't finds any commands related to your query")






 
