import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir! Please tell how may i help you")            



def takeCommand():
    #it takes microphone input from user and return string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,"en-in")
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)

        print("say that again please...")
        return "None"    
    return query



def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.alho()
    server.starttls()
    server.login('sourabhm384@gmail.com','Sourabh@12')
    server.sendemail('sourabhm384@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query =  query.replace("wikipedia","")
            results = wikipedia.summery(query,sentence=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open music' in query:
            music_dir = "D:\\music\\Favourite Song"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 
        elif 'open code' in query:
            codePath = "C:\\Users\\sourabh.mishra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to' in query:
            try:
                speak("what should i say ?")
                content = takecommand()
                to = "sourabhrishabhmishra@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend sourabh. I am not able to send this email")              