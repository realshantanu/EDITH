import pyttsx3 #pip install pyttsx3
import datetime 
import wikipedia #pip insstall wikipedia
import webbrowser
import os
import sys
import random
import urllib.request#used to request to webbrower #pip install urllib
import urllib.parse#used to split the query
import re#give special charater necessary for search
import smtplib #pip install smtplib
from email.mime.multipart import MIMEMultipart#Multipurpose Internet Mail Extensions (MIME)
from email.mime.text import MIMEText
import urllib.request
from joke.jokes import *  #pip install axju-jokes
import time 
from tkinter import *  
from translate import Translator #pip install translate
import requests #pip install requests
from pyautogui import press
from time import sleep
import numpy as np
from math import inf as infinity





def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
print("[INTERNET] - [CONNECTED]" if connect() else "[INTERNET] - [NOT CONNECTED] Connect To Internet to use more commands.")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Connected" if connect() else "No internet! Connect To Internet to use more commands.")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Sir Please tell me how may I help you")       

speak(wishMe())
print('''

░██╗░░░░░░░██╗███████╗██████╗░███╗░░██╗███████╗░██████╗██████╗░░█████╗░██╗░░░██╗
░██║░░██╗░░██║██╔════╝██╔══██╗████╗░██║██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░██║░░██║██╔██╗██║█████╗░░╚█████╗░██║░░██║███████║░╚████╔╝░
░░████╔═████║░██╔══╝░░██║░░██║██║╚████║██╔══╝░░░╚═══██╗██║░░██║██╔══██║░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗██████╔╝██║░╚███║███████╗██████╔╝██████╔╝██║░░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

Type "Help" for help.

''')
while True:

    query = input("Your Command:  ")
    query = query.lower()
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    
    if 'wikipedia' in query:
        try:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
        
        
    elif 'open youtube' in query:
        try:
            webbrowser.open("www.youtube.com")
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
        
    elif 'open whatsapp' in query:
        try:
            webbrowser.open("https:\\web.whatsapp.com")
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
        
    elif 'open insta' in query:
        try:
            webbrowser.open("https:\\www.instagram.com")
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
    
    elif 'open google' in query:
        try:
            webbrowser.open("www.google.com")
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
    
    elif 'what is the time' in query:
        t = hour,"hour and",minute,"minutes"
        print(hour,"hour and",minute,"minutes")
        speak(t)
    
    elif "play movie" in query:
        movie_dir = "E:"
        movie = os.listdir(movie_dir)
        print(movie)
        m = int(input("which movie you want to play eg 0 for 1st movie:  "))
        if m>len(movie):
            a = "Invalid entry!,Movie",m,"Do not Exists."
            print(a)
            speak(a)
        elif m<=len(movie):
            os.startfile(os.path.join(movie_dir, movie[m]))
    
    elif "play music" in query:
        songs_dir = "C:\\Users\\Shantanu\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        n = int(input("which song you want to play eg 0 for 1st Song:  "))
        if n>len(songs):
            a = "Invalid entry!,Song",n,"Do not Exists."
            print(a)
            speak(a)
        elif n<=len(songs):
            os.startfile(os.path.join(songs_dir, songs[n]))
    
    elif 'quit' in query:
        print("Bye-Bye Sir!")
        speak("Bye-Bye Sir!")
        sys.exit(0)
        
    elif 'shutdown' in query:
        shutdown_dir = "C:\\Users\\Shantanu\\Desktop\\EDITH\\bat files\\shutdown.bat"
        
        hour = int(datetime.datetime.now().hour)
        
        if hour>=0 and hour<12:
            print("Have a Nice Day Sir!")
            speak("Have a Nice Day Sir!")
        
        elif hour>=12 and hour<18:
            print("Time To Take Powernap Sir!")
            speak("Time To Take Powernap Sir!")   
        
        else:
            print("Good Night! Sir")
            speak("Good Night! Sir")
        speak("ShuttingDown your PC!")
        os.startfile(os.path.join(shutdown_dir))
        
    elif 'restart' in query:
        restart_dir = "C:\\Users\\Shantanu\\Desktop\\EDITH\\bat files\\restart.bat"
        print("Restarting your PC!")
        speak("Restarting your PC!")
        os.startfile(os.path.join(restart_dir))
        
    elif 'toss a coin' in query:
        a = ["Head","Tail"]
        b = random.choice(a)
        print(b)
        speak(b)
    
    elif 'on google' in query:
        try:
            a=input("Enter what you want to search for:")
            ur="https://www.google.com/search?q="
            webbrowser.open_new(ur+a)
            
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
    
    elif 'on youtube' in query:
        try:
            search_keyword= input("Enter Query You Want To Search:   ")
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
            print("https://www.youtube.com/watch?v=" + video_ids[0])
        except:
            print("Connection Error!!")
            speak("Connection Error!!")
    
    
    elif 'send mail' in query:
        try:
            mail_content = input("Enter The Message:  ")
            sender_address = 'shantanurajmane21@gmail.com'
            sender_pass = '9527226630'
            receiver_address = input('Enter receviers mail Eg:receiver567@gmail.com:   ')
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = input("Enter Subject Of Mail:  ")
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
            speak('Mail Sent')
        except:
            print("Something Went Wrong!! Mail Not Send.")
            speak("Something Went Wrong!! Mail Not Send.")
      
        
    elif 'tell me a joke' in query:
        try:
            from random import choice
            a = choice([geek, icanhazdad, chucknorris, icndb])()
            print(a)
            speak(a)
        except:
            print("Connection Error!!!")
            speak("Connection Error!!!")
    
    elif 'set timer' in query:
        second = int(input("How long to wait?(in Seconds):  "))
        for i in range(second):
            a = second - i
            print(a)
            time.sleep(1)
            
    elif 'weather' in query:
        try:
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=f9586d0b1005dd472de99a9badc41409&q='
            city = input('City Name :')
            url = api_address + city
            json_data = requests.get(url).json()
            format_add = json_data['main']
            print(format_add)
        except:
            print("Connection Error!!!")
            speak("Connection Error!!!")
    
    elif 'translate' in query:
        try:
            Text = input("Text To Translate:  ")
            To_Lang = str(input("Enter Name of Language:  "))
            translator= Translator(to_lang=To_Lang)
            translation = translator.translate(Text)
            print(translation)
            speak(translation)
        except:
            print("Connection Error!!!")
            speak("Connection Error!!!")
        
    elif 'bedtime story' in query:
        story_dir = "C:\\Users\\Shantanu\\Desktop\\EDITH\\stories"
        story = os.listdir(story_dir)
        print(story)
        m = int(input("which story you want to listen:  "))
        if m>len(story):
            a = "Invalid entry!,Movie",m,"Do not Exists."
            print(a)
            speak(a)
        elif m<=len(story):
            with open(os.path.join(story_dir, story[m])) as f:
                for line in f:
                    engine.setProperty('rate',150)
                    print(line.strip())
                    speak(line.strip())
                    
                shutdown_dir = "C:\\Users\\Shantanu\\Desktop\\EDITH\\bat files\\shutdown.bat"
                hour = int(datetime.datetime.now().hour)
                
                if hour>=0 and hour<12:
                    print("Have a Nice Day Sir!")
                    speak("Have a Nice Day Sir!")
                    
                elif hour>=12 and hour<18:
                    print("Time To Take Powernap Sir!")
                    speak("Time To Take Powernap Sir!")   
                    
                else:
                    print("Good Night! Sir")
                    speak("Good Night! Sir")
                    
                speak("ShuttingDown your PC!")
                sleep(2)
                os.startfile(os.path.join(shutdown_dir))
                
    elif 'password' in query:
        print('''Password Generator
==================''')
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
        number = input('number of passwords?')
        number = int(number)
        
        length = input('password length?')
        length = int(length)
        
        print('\nhere are your passwords:')
        for pwd in range(number):
            password = ''
            for c in range(length):
                password += random.choice(chars)
            print(password)
            
    
    elif 'screenshot' in query:
        press("printscreen")
        
    elif "who are you" in query:
        print("WEDNESDAY, Your Personal Assistent!")
        speak("WEDNESDAY, Your Personal Assistent!");
        
    elif "xo" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\game\\Tic-Tac-Toe-Game-in-python-3-Tkinter-master\\my tic tac 2.py")
        read_file = stream.read()
        exec(read_file);
    
    elif "2048" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\game\\2048\\2048.py")
        read_file = stream.read()
        exec(read_file);
    
    elif "hash" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\hash.py")
        read_file = stream.read()
        exec(read_file);
        
    elif "help" in query:
        print('''
COMMANDS:                       | SYNTEX:
[1] Wikipedia                   |[1] wikipedia <query to search>
[2] Open Youtube                |[2] open youtube
[3] Open Google                 |[3] open google
[4] Time                        |[4] what is the time
[5] Search On Google            |[5] search on google
[6] Search On Youtube           |[6] search on youtube
[7] Send Mail                   |[7] send mail
[8] Tell Me Joke                |[8] tell me a joke
[9] Set Timer                   |[9] set timer
[10] Weather                    |[10] weather
[11] Translate                  |[11] translate
[12] Bed Time Stories           |[12] bedtime story
[13] Password Generator         |[13] generate password
[14] ScreenShot                 |[14] screenshot
[15] Game                       |[15] play xo , play 2048
[16] Music                      |[16] play music
[17] Movies                     |[17] play movie
[18] MD5 Hash Convertor         |[18] MD5 hash
[19] ChatBot                    |[19] chat with me
[20] Latest News                |[20] news
[21] Youtube Video Downloader   |[21] download youtube video
[22] WhiteBoard                 |[22] open whiteboard
[23] Youtube Video In Audio For.|[23] mp3 downloader
[24]Open Whatsapp               |[24]open Whatsapp
[25]Open Instagram              |[25]open insta
[26]Battery Status              |[26]check battery status
        ''')
    
    elif "chat" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\chatbot.py")
        read_file = stream.read()
        exec(read_file);
        
    elif "news" in query:
        try:
            stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\news.py")
            read_file = stream.read()
            exec(read_file)
        except:
            print("Connection Error!!!")
            speak("Connection Error!!!")
        
        
    elif "my ip" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\IpFinder.py")
        read_file = stream.read()
        exec(read_file);
        
    elif "download youtube video" in query:
        try:
            stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\youtube_video_downloader.py")
            read_file = stream.read()
            exec(read_file);
        except:
            print("Download Failed!!")
            speak("Download Failed!!")
    
    elif "whiteboard" in query:
        try:
            webbrowser.open("https://www.twiddla.com/xdkrng")
            
        except:
            print("Connection Error!!!")
            speak("Connection Error!!!")
    
    
    elif "mp3 downloader" in query:
        try:
            stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\mp3_downloader.py")
            read_file = stream.read()
            exec(read_file);
            print("Download Success!")
            speak("Download Success!")
        except:
            print("Download Failed!!")
            speak("Download Failed!!")
        
    
    elif 'check battery status' in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\power_status.py")
        read_file = stream.read()
        exec(read_file)
        
    
    else:
        c = "No Command Assigned for",query
        print(c)
        speak(c)
