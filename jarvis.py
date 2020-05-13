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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▀▀█▀▀ ▒█░▒█ 
▒█▀▀▀ ▒█░▒█ ▒█░ ░▒█░░ ▒█▀▀█ 
▒█▄▄▄ ▒█▄▄▀ ▄█▄ ░▒█░░ ▒█░▒█

Type "Help" for help.

''')
while True:
    query = input("Your Command:  ")
    query = query.lower()
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        
        
    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("www.google.com")
    
    elif 'what is the time' in query:
        t = hour,"hour and",minute,"minutes"
        print(hour,"hour and",minute,"minutes")
        speak(t)
    
    elif "play movie" in query:
        movie_dir = "E:"
        movie = os.listdir(movie_dir)
        print(movie)
        m = int(input("which movie you want to play eg 0 for 1st song:  "))
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
        a=input("Enter what you want to search for:")
        ur="https://www.google.com/search?q="
        webbrowser.open_new(ur+a)
    
    elif 'on youtube' in query:
        query_string = urllib.parse.urlencode({"search_query" : input("Query: ")})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
    
    
    elif 'send mail' in query:
        mail_content = input("Enter The Message:  ")
        sender_address = 'Enter Your Mail Address'
        sender_pass = 'Enter Your Mail Password'
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
      
        
    elif 'tell me a joke' in query:
        from random import choice
        a = choice([geek, icanhazdad, chucknorris, icndb])()
        print(a)
        speak(a)
    
    elif 'set timer' in query:
        second = int(input("How long to wait?(in Seconds):  "))
        for i in range(second):
            a = second - i
            print(a)
            time.sleep(1)
            
    elif 'weather' in query:
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=f9586d0b1005dd472de99a9badc41409&q='
        city = input('City Name :')
        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data['main']
        print(format_add)
    
    elif 'translate' in query:
        Text = input("Text To Translate:  ")
        To_Lang = str(input("Enter Name of Language:  "))
        translator= Translator(to_lang=To_Lang)
        translation = translator.translate(Text)
        print(translation)
        speak(translation)
        
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
        print("EDITH, Your Personal Assistent!")
        speak("EDITH, Your Personal Assistent!");
        
    elif "game" in query:
        game_state = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]
        
        players = ['X','O']
        
        def play_move(state, player, block_num):
            if state[int((block_num-1)/3)][(block_num-1)%3] is ' ':
                state[int((block_num-1)/3)][(block_num-1)%3] = player
            
            else:
                block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
                play_move(state, player, block_num)
                
        def copy_game_state(state):
            new_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            for i in range(3):
                for j in range(3):
                    new_state[i][j] = state[i][j]
            return new_state
        
        def check_current_state(game_state):
            # Check if draw
            draw_flag = 0
            for i in range(3):
                for j in range(3):
                    if game_state[i][j] is ' ':
                        draw_flag = 1
            if draw_flag is 0:
                return None, "Draw"
            # Check horizontals
            if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
                return game_state[0][0], "Done"
            if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
                return game_state[1][0], "Done"
            if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
                return game_state[2][0], "Done"
        
        # Check verticals
            if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
                return game_state[0][0], "Done"
            if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
                return game_state[0][1], "Done"
            if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
                return game_state[0][2], "Done"
        # Check diagonals
            if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
                return game_state[1][1], "Done"
            if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
                return game_state[1][1], "Done"
        
            return None, "Not Done"
    
        def print_board(game_state):
            print('----------------')
            print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |')
            print('----------------')
            print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |')
            print('----------------')
            print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |')
            print('----------------')
            
        def getBestMove(state, player):
            '''
            Minimax Algorithm
            '''
            winner_loser , done = check_current_state(state)
            if done == "Done" and winner_loser == 'O': # If AI won
                return 1
            elif done == "Done" and winner_loser == 'X': # If Human won
                return -1
            elif done == "Draw":    # Draw condition
                return 0
            
            moves = []
            empty_cells = []
            for i in range(3):
                for j in range(3):
                    if state[i][j] is ' ':
                        empty_cells.append(i*3 + (j+1))
            
            for empty_cell in empty_cells:
                move = {}
                move['index'] = empty_cell
                new_state = copy_game_state(state)
                play_move(new_state, player, empty_cell)
                
                if player == 'O':    # If AI
                    result = getBestMove(new_state, 'X')    # make more depth tree for human
                    move['score'] = result
                else:
                    result = getBestMove(new_state, 'O')    # make more depth tree for AI
                    move['score'] = result
                
                moves.append(move)
            # Find best move
            best_move = None
            if player == 'O':   # If AI player
                best = -infinity
                for move in moves:
                    if move['score'] > best:
                        best = move['score']
                        best_move = move['index']
            
            else:
                best = infinity
                for move in moves:
                    if move['score'] < best:
                        best = move['score']
                        best_move = move['index']
            
            return best_move
        # PLaying
        play_again = 'Y'
        while play_again == 'Y' or play_again == 'y':
            game_state = [[' ',' ',' '],
                          [' ',' ',' '],
                          [' ',' ',' ']]
            current_state = "Not Done"
            print("\nNew Game!")
            print_board(game_state)
            player_choice = input("Choose which player goes first - X (You - the petty human) or O(The mighty AI): ")
            winner = None
            
            if player_choice == 'X' or player_choice == 'x':
                current_player_idx = 0
                
            else:
                current_player_idx = 1
                
            while current_state == "Not Done":
                if current_player_idx == 0: # Human's turn
                    block_choice = int(input("Oye Human, your turn! Choose where to place (1 to 9): "))
                    play_move(game_state ,players[current_player_idx], block_choice)
                else:   # AI's turn
                    block_choice = getBestMove(game_state, players[current_player_idx])
                    play_move(game_state ,players[current_player_idx], block_choice)
                    print("AI plays move: " + str(block_choice))
                print_board(game_state)
                winner, current_state = check_current_state(game_state)
                if winner is not None:
                    print(str(winner) + " won!")
                else:
                    current_player_idx = (current_player_idx + 1)%2
                
                if current_state is "Draw":
                    print("Draw!")
            
            play_again = input('Wanna try again BIYTACH?(Y/N) : ')
            if play_again == 'N':
                print('Nice Game!!')
                
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
[15] Game                       |[15] game
[16] Music                      |[16] play music
[17] Movies                     |[17] play movie
[18] MD5 Hash Convertor         |[18] MD5 hash
[19] ChatBot                    |[19] chat with me
[20] Latest News                |[20] news
[21] Youtube Video Downloader   |[21] download youtube video
        ''')
    
    elif "chat" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\chatbot.py")
        read_file = stream.read()
        exec(read_file);
        
    elif "news" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\news.py")
        read_file = stream.read()
        exec(read_file);
        
    elif "download youtube video" in query:
        stream = open("C:\\Users\\Shantanu\\Desktop\\EDITH\\youtube_video_downloader.py")
        read_file = stream.read()
        exec(read_file);
        
    
    
    
    else:
        c = "No Command Assigned for",query
        print(c)
        speak(c)
