import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import sys
import pyjokes
import json
import requests
from urllib.request import urlopen

import time
import os


try:
    engine = pyttsx3.init()


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def time_():
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("the current time is")
        speak(Time)

    def wishme():
        speak("Welcome back")
        hour = datetime.datetime.now().hour

        if hour >= 6 and hour < 12:
            speak("good morning sir")
        elif hour >= 12 and hour < 18:
            speak("good afternoon sir")
        elif hour >= 18 and hour < 24:
            speak("good evening sir")
        else:
            speak("good night sir")

        speak("tell me how i can help you today")

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("recognizing....")
            query = r.recognize_google(audio,language='en-US')
            print(query)

        except Exception as e:
            print(e)
            print("say that again please")
            return "None"
        return query

    def joke():
        speak(pyjokes.get_joke())

    if __name__ == "__main__":
        wishme()
        while True:
            query = takeCommand().lower()
            if 'time' in query:
                time_()

            elif 'your creator' in query:
                speak("my creator is mr. rofi")

            elif 'how are you' in query:
                for i in range(1, 4):
                    speak("halo mr. rofi, im fine")

            elif 'wikipedia' in query:
                speak("searching....")
                query = query.replace('wikipedia','')
                result = wikipedia.summary(query, sentences=3)
                speak("acording to wikipedia")
                print(result)
                speak(result)

            elif 'search in chrome' in query:
                speak("what should i search?")
                chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search+'.com')

            elif 'search youtube' in query:
                speak("what should i search?")
                searchyt = takeCommand().lower()
                speak("here we go to youtube")
                wb.open('https://www.youtube.com/results?search_query='+searchyt)

            elif 'search google' in query:
                speak("what should i search?")
                searchgl = takeCommand().lower()
                speak("searching")
                wb.open('https://www.google.com/search?q='+searchgl)

            elif 'joke' in query:
                joke()
            
            elif 'offline' in query:
                speak("going offline")
                quit()

            elif 'write notes' in query:
                speak("what should i write sir?")
                notes = takeCommand()
                file = open('notes.txt', 'w')
                speak("sir should i include date and time?")
                ans = takeCommand()
                if 'yes' in ans or 'sure' in ans:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(':-')
                    file.write(notes)
                    speak("done taking notes sir")
                else:
                    file.write(notes)
            
            elif 'show notes' in query:
                speak("showing notes")
                file = open('notes.txt', 'r')
                print(file.read())
                speak(file.read())

            elif 'where is' in query:
                query = query.replace("where is","")
                location = query
                speak("user asked to locate"+location)
                wb.open_new_tab("https://www.google.com/maps/place/"+location)

            elif 'stop listening' in query:
                speak("for how many secound you want me to stop listening to your commands?")
                ans = int(takeCommand())
                time.sleep(ans)
                print(ans)

            elif 'signing out' in query:
                speak("signing out")
                os.system("shutdown -l")

except KeyboardInterrupt:
    print("exit the program")
    speak("exit the program")
    sys.exit()
