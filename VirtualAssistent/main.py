import os
import pyttsx3
import speech_recognition as sr
import datetime
import random
import wikipedia
import webbrowser
import pyjokes
import subprocess
import time
import pyautogui
import psutil
import winshell
import sys
import imdb
import string
from calendar import *
from cam import *
import socket
from GoogleNews import GoogleNews
import pandas as pd


def password():
    char = string.ascii_letters + string.digits
    ret = "".join(random.choice(char) for x in range(15))
    return ret

print(password())

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def news():
    googlenews = GoogleNews(period='id')
    googlenews.search('Albania')
    result = googlenews.result()
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns=['img'])
    data.head()

    for i in result:
        speak(i['title'])


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en')
            print(f"User said: {query}\n")
        except Exception as e:
            speak("Unable to recognize your voice......")
            return "None"
        return query


def username():
    speak("How should I call you?")
    name = takeCommand()
    speak("Welcome " + name)
    speak("How can I help you?")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning!')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon!')
    else:
        speak('Good evening!')
    speak("I am your virtual assistant.")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage + '%')
    battery = str(psutil.sensors_battery().percent)
    speak('Battery is at ' + battery + '%')


def movie():
    moviesdb = imdb.IMDb()
    speak('Please tell me the movie name')
    text = takeCommand()
    movies = moviesdb.search_movie(text)
    speak('Searching...')
    if len(movies) == 0:
        speak('No result found')
    else:
        speak('I found these:')
        for movie in movies:
            title = movie['title']
            year = movie['year']
            speak(f'{title} - {year}')
            info = movie.movieID
            movie = moviesdb.get_movie(info)
            rating = movie['rating']
            plot = movie['plot outline']
            if year < int(datetime.datetime.now().strftime("%Y")):
                speak(f'{title} was released in {year}, has an IMDb rating of {rating}. The plot summary of the movie is {plot}')
            else:
                speak(f'{title} will be released in {year}, has an IMDb rating of {rating}. The plot summary of the movie is {plot}')
            break


def rock():
    you = int(input('Please enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissor\n'))
    shapes = {1: 'rock', 2: 'paper', 3: 'scissor'}
    
    if you not in shapes:
        print('Please enter a valid number')
        return 
    
    comp = random.randint(1, 3)
    print('You chose', shapes[you])
    print('Computer chose', shapes[comp])
    
    if (you == 1 and comp == 3) or (you == 2 and comp == 1) or (you == 3 and comp == 2):
        print('Congratulations, you won!')
    elif you == comp:
        print('Match tied!')
    else:
        print('You lost!')



def count():
    t=int(input('Enter the time in seconds'))
    while t:
        min, secs=divmod(t, 60)
        timer='(:02d):(:02d)'.format(min, secs)
        print(timer, end='\r')
        time.sleep(1)
        t-=1
        print('\n')


if __name__ == '__main__':
    wishMe()
    username()
    while True:
        order = takeCommand().lower()

        if 'how are you' in order:
            speak("I am fine, thank you!")
            speak("How are you?")

        elif 'fine' in order or 'good' in order:
            speak("Good to know")

        elif 'who am I' in order:
            speak("If you can talk, you surely are a human")

        elif 'play music' in order or 'play songs' in order:
            music_dir = "E:\\Songs\\New folder"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'wikipedia' in order:
            speak('Searching....')
            order = order.replace("wikipedia", "")
            results = wikipedia.summary(order, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open google' in order:
            speak('Here you go to Google')
            webbrowser.open("google.com")

        elif 'open amazon' in order:
            speak('Here you go to Amazon')
            webbrowser.open("amazon.com")

        elif 'open youtube' in order:
            speak('Here you go to YouTube')
            webbrowser.open("youtube.com")

        elif 'where is' in order:
            order = order.replace('where is', '')
            location = order
            speak('Locating.....')
            speak(location)
            webbrowser.open('https://www.google.com/maps/place/' + location)

        elif 'jokes' in order or 'joke' in order:
            speak(pyjokes.get_joke(language='en', category='neutral'))

        elif 'time' in order:
            time_str = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Time is : {time_str}')

        elif 'shut down' in order or 'turn off' in order:
            speak('Hold on! The system is on its way to shut down')
            speak('Make sure all applications are closed')
            time.sleep(5)
            subprocess.call(['shutdown', '/s'])

        elif 'restart' in order:
            speak('Restarting device')
            subprocess.call(['shutdown', '/r'])

        elif 'hibernate' in order:
            speak('Hibernating')
            subprocess.call(['shutdown', '/h'])

        elif 'log out' in order or 'sign out' in order:
            speak('Make sure all applications are closed')
            time.sleep(5)
            subprocess.call(['shutdown', '/l'])

        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'screenshot' in order:
            speak('Please, tell me the name for this file')
            name = takeCommand().lower()
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f'{name}.png')
            speak('Screenshot captured')

        elif 'cpu status' in order:
            cpu()

        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak('Done')

        elif 'camera' in order:
            cam()

        elif 'exit' in order or 'stop' in order or 'quit' in order:
            speak('Thank you for using me! Have a nice day!')
            sys.exit()

        elif 'ip' in order:
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            speak('Your IP address is ' + ip)

        elif 'bmi' in order:
            speak('Please tell your height in centimeters')
            height = takeCommand()
            speak('Please tell your weight in kilograms')
            weight = takeCommand()
            height = float(height) / 100
            BMI = float(weight) / (height * height)
            speak('Your Body Mass Index (BMI) is ' + str(BMI))
            if BMI > 0:
                if BMI <= 16:
                    speak('You are severely underweight')
                elif BMI <= 18.5:
                    speak('You are underweight')
                elif BMI <= 25:
                    speak('You are healthy')
                elif BMI <= 30:
                    speak('You are overweight')
                else:
                    speak('You are severely overweight')
            else:
                speak('Invalid data')

        elif 'movie' in order:
            movie()

        elif 'news' in order:
            news()

        elif 'password' in order:
            speak(password())

        elif 'rock' in order:
            rock()

        elif 'countdown' in order:
            count()        
