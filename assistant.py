import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys
import os
import smtplib
import pyautogui
import pywhatkit as kit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greetMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morning,sir")
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        print("Good Afternoon,sir")
        speak("Good Afternoon,sir ")
    else:
        print("Good Evening,sir")
        speak("Good Evening,sir")
        speak(" I am Siri, How can I help you ?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshhold=400
        audio=r.listen(source,0,4)
    try:
        print("Recognizing.....")
        speak("Recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"you said:{query}\n")
    except Exception as e:
        print("Say That Again....")
        speak("Say That Again")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('noreply@gmail.com','Interstellar')
    server.sendmail('noreply@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    greetMe()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            quer=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath=r"C:\Users\91905\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("what should I send")
                content=takeCommand()
                to="mran@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
                print("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend, I am not able to send the email")
                print("sorry my friend, I am not able to send the email")
        elif 'play my album' in query:
            music_dir=r'C:\Users\91905\Music\Playlists'
            playlists=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, playlists[8]))
        elif 'play music' in query:
            speak('Which song you wanna play')
            print("which song you wanna play")
            try:
                cm=takeCommand()
                kit.playonyt(f"{cm}")
            except:
                speak("please repeat the song name")
                print("please repeat the song name")
        elif "pause" in query:
            pyautogui.press("space bar")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("space bar")
            speak("video played")
        elif 'siri sleep' in query:
            print("Have a good day,Sir")
            speak("Have a good day,Sir")
            sys.exit();
