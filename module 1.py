import pyttsx3
import speech_recognition as sr
import datetime
import os 
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                speak("Please speak.......")
                r.pause_threshold = 0.8
                audio = r.listen(source)

        try:
                speak("Recognizing.........")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said :{query}")
        


        except Exception as e:
                speak("Please say that again...")
                return "none"
        return query
if __name__ == "__main__":
        while True:
        #if 1: 
                query = takeCommand().lower()
                if 'thank you' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\thank-you-simax.gif"
                        os.startfile(codePath)
                        query = takeCommand().lower()
                if 'module 2' in query:
                        speak("you have selected module two so i request you to create the hand gestures")
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleTwo\\main.py"
                        os.startfile(codePath)
                        query = takeCommand().lower()
                if 'cool' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\cool-sign.gif"
                        os.startfile(codePath)
                        query = takeCommand().lower()
                if 'how are you' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\how-are-you-deaf.gif"
                        os.startfile(codePath)
                if 'nice to meet you ' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\nice-to-meet-you-deaf.gif"
                        os.startfile(codePath)
                if 'wonderful' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\wonderful-simax.gif"
                        os.startfile(codePath)
                if 'yes' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\yes-sign.gif"
                        os.startfile(codePath)
                if 'super' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\super-simax.gif"
                        os.startfile(codePath)
               
                if 'please' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\please-simax.gif"
                        os.startfile(codePath)
                
                if 'sorry' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\sorry-sign.gif"
                        os.startfile(codePath)
                if 'keep calm' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\simax-sign-time.gif"
                        os.startfile(codePath)
                if 'drshti' in query:
                        codePath = "C:\\Users\\edlab\\Project VISION\\moduleOne\\dataSet\\simax-sign-time.gif"
                        os.startfile(codePath)
                elif "shut down" in query:
                        speak("okay, i am taking leave....... Thank you for using me...")
                        sys.exit()

                speak("do you have any other work?")
