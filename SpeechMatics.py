import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
        

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
           

    else:
        print("Good Evening!")
        speak("Good Evening!")  
        

    print("Welcome sir,I am your Assistent How may i help you") 
    speak("Welcome sir,I am your Assistent How may i help you") 
          

def takeCommand():
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
        print("Say that again please...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abcdkumar2401@gmail.com', 'moto10otom*')
    server.sendmail('harryyy01@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\harry\\OneDrive\\Desktop\\song\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
            
        
        elif 'your name' in query:   
            print("Sir, my name is Jarvis")
            speak("Sir, my name is Jarvis")

        elif 'my name' in query:   
            print("Sir, as you told me your name is harshit")
            speak("Sir, as you told me your name is harshit")
            
        
        elif 'my age' in query:  
            print("sir your age is 22")
            speak("sir your age is 22")


        elif 'exit' in query:
            print("ok sir")
            speak("Ok Sir")
            exit()
        elif 'bye' in query:
            print("Bye,Sir Happy to help you ")
            speak("Bye,Sir Happy to help you ")
            exit()
        elif 'close' in query:
            print("Closing Sir")
            speak("Closing Sir ")
            exit()
        elif 'stop' in query:
            speak("Ok Sir ")
            exit() 
        elif 'email to harry' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                
                content = takeCommand()
                to = "harryyy01@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
                print("Sorry my friend harry bhai. I am not able to send this email")           


       