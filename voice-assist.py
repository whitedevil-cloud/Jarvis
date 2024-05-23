import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
recognizer=sr.Recognizer()



def cmd():
    with sr.Microphone() as source:
        print('Clearing background noices...Please Wait...')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
             
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)

    if 'open chrome' in command:
        engine.say('Opening chrome wait')
        engine.runAndWait()
        program="C:\Program Files\Google\Chrome\Application"
        subprocess.Popen([program])
        print(*a[1:5],sep=',')
    
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

#cmd()
