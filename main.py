"""
Main File containing all the management process
"""

import webbrowser
from datetime import datetime
import time

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty("voices")


def speak(audio):
    """
    This function speaks out the output
    """
    engine.say(audio, voices[0].id)
    engine.runAndWait()


def take_command():
    """
    Recognises commands from the speech
    """
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # speech.pause_threshold = 1
        audio = speech.listen(source)
        try:
            print("Recognizing ...")
            query = speech.recognize_google(audio, language="en-in")
            print(query)
            return query.lower()
        except Exception as exception:
            print(exception)
            speak("Say that again please..")
            return None


def wish_me():
    """
    Welcome message for the owners
    """
    hour = int(datetime.now().hour)
    print(hour)
    if 0 < hour < 12:
        speak("Good Morning, Abhishek")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Abhishek")
    else:
        speak("Good Evening, Abhishek")

    speak("How can I help you ?")


def execute_query(query):
    """
    This function executes the query
    """
    if "wikipedia" in query:
        speak("Searching in wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=10)
        speak("According to wikipedia, " + results)
    elif "youtube" in query:
        speak("Searching in youtube...")
        query = query.replace("in youtube", "")
        results = webbrowser.open_new_tab("https://youtube.com")
    elif "google" in query:
        results = webbrowser.open_new_tab("https://google.com")
    elif "facebook" in query:
        results = webbrowser.open_new_tab("https://facebook.com")
    elif "linkedin" in query:
        results = webbrowser.open_new_tab("https://linkedin.com")
    elif "gmail" in query:
        results = webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    print(results)


def jericho():
    """
    main function which executes the complete process
    """
    wish_me()
    status = True
    while status:
        query = take_command()
        if not query or "exit" in query:
            status = False
            continue
        execute_query(query)
        time.sleep(300)


jericho()
