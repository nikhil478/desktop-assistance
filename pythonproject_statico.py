import pyttsx3
import datetime
import os
import speech_recognition as sr
import wikipedia
import webbrowser
#import smtplib



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)


def speak(audio):
    """"input = string value and returns voice"""
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=4 and hour <= 8:
        speak("good morning sr")
        print("good morning sr")
    elif hour >= 9 and hour <= 16:
        speak("good afternoon sr")
        print("good afternoon sr")
    elif hour >= 17 and hour <= 20:
        speak("good evening sr")
        print("good evening sr")
    else:
        speak("good night sr")
        print("good night")
        

        

def takecommand():
    """ input - microphone voice and output strng """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        r.adjust_for_ambient_noise(source, duration=3)
        audio = r.listen(source)
        
    try:
        print("Recoginizing...")
        query = r.recoginize_google(audio , language = "en-in")
        print("you said:" , query)
        
    except Exception:
        print("say that again")
        return "none"
    return query


while True:
    query = takecommand().lower()
    
    
    
    if "wikipedia" in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia" , "")
        results = wikipedia.summary(query , sentences = 1)
        speak(results)
        print(results)
    
    elif "open youtube" in query:
        speak("opening youtube")
        if query == "open youtube":
            webbrowser.open("youtube.com")
        elif query.replace("open youtube",""):
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
            
    elif "open google" in query:
        speak("google is opening...")
        webbrowser.open("google.com")
        
    elif "open github" in query:
        webbrowser.open("https://github.com/nikhil478")
        
    elif "open twitter" in query:
        webbrowser.open("twitter.com")
        
    elif "open whatsapp" in query:
        webbrowser.open("whatsapp.com") 
        
    elif "search" in query:
        query = query.replace("search","")
        webbrowser.open(query+".com")
        
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
        
    elif "play music" in query:
        music_dir = "E:\music"
        songs = os.listdir(music_dir)
        print(songs)
        a = int(input("enter your song number"))
        os.startfile(os.path.join(music_dir,songs[a]))
        
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("the time is",strTime)
        
        
        
        
        
    
        
        
    
        
        
