import pyttsx3
import speech_recognition as sr
import datetime
import os 
import sys
import cv2
import mediapipe as mp

def mod1():
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        print(voices[1].id)
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
                                mod2()
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
def mod2():
        my_list = []
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        print(voices[1].id)
        engine.setProperty('voices', voices[1].id)
        def speak(audio):
                engine.say(audio)
                engine.runAndWait()

        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils
        cap = cv2.VideoCapture(0)

        finger_tips = [8, 12, 16, 20]
        thumb_tip = 4

        # like_img = cv2.imread("images/like.png")
        # like_img = cv2.resize(like_img, (200, 180))
        #
        # dislike_img = cv2.imread("images/dislike.png")
        # dislike_img = cv2.resize(dislike_img, (200, 180))

        while True:
                ret, img = cap.read()
                img = cv2.flip(img, 1)
                h, w, c = img.shape
                results = hands.process(img)

                if results.multi_hand_landmarks:
                        for hand_landmark in results.multi_hand_landmarks:
                                lm_list = []
                        for id, lm in enumerate(hand_landmark.landmark):
                                lm_list.append(lm)
                        finger_fold_status = []
                        for tip in finger_tips:
                                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                                # print(id, ":", x, y)
                                #cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)

                                if lm_list[tip].x < lm_list[tip - 2].x:
                                #cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                                        finger_fold_status.append(True)
                                else:
                                        finger_fold_status.append(False)

                        print(finger_fold_status)

                        x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
                        print(x, y)
                        # fuck off
                        if lm_list[3].x < lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                                cv2.putText(img, "fuck off !!!", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                speak("fuck off")
                        

                        # one
                        if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                                cv2.putText(img, "ONE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("1")
                                speak("one......................")
                        #two
                        if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                                cv2.putText(img, "TWO", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                speak("two.....................")
                                my_list.append("2")
                        #three
                        if lm_list[2].x < lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                                cv2.putText(img, "THREE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("3")
                                speak("three.....................")
                        #four
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[2].x < lm_list[8].x:
                                cv2.putText(img, "FOUR", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("4")
                                speak("four.....................")
                        # five
                        if lm_list[2].x < lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                                lm_list[5].x:
                                cv2.putText(img, "FIVE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("5")
                                speak("five.....................")                           
                        # six
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y < lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                                lm_list[5].x:
                                cv2.putText(img, "SIX", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("6")
                                speak("SIX.....................")
                        #SEVEN
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y > lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                                lm_list[5].x:
                                cv2.putText(img, "SEVEN", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("7")
                                speak("SEVEN.....................")
                        #EIGHT
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                                lm_list[5].x:
                                cv2.putText(img, "EIGHT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("8")
                                speak("EIGHT.....................")
                        #NINE
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                                lm_list[5].x:
                                cv2.putText(img, "NINE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("9")
                                speak("NINE.....................")
                        #A
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                                lm_list[5].x:
                                cv2.putText(img, "A", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("A")
                                speak("A")
                        #B
                        if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[2].x > lm_list[8].x:
                                cv2.putText(img, "B", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                                my_list.append("B")
                                speak("B.....................")
                        mp_draw.draw_landmarks(img, hand_landmark,
                                                mp_hands.HAND_CONNECTIONS,
                                                mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                                mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                                )
                my_sentense = ''.join(my_list)                
                #cv2.putText(img, my_sentense, (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)
                cv2.imshow("SIGN LANGUAGE DETECTION - SAMEER EDLABADKAR", img)
                cv2.waitKey(1)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()
def wishMe():
        hour = int(datetime.datetime.now().hour)
        
        if hour>=0 and hour<12:
                speak("good morning, welcome to the project vision. we are working on two different modals where we communicate with those persons who can not speak, listen, see the things. you have to select the module. please say module 1 for normal to impaired person and module 2 for impaired to disabled...have a good conversation, thank you. ")

        elif hour>=12 and hour<18:
                speak("good afternoon, welcome to the project vision. we are working on two different modals where we communicate with those persons who can not speak, listen, see the things. you have to select the module. please say module 1 for normal to impaired person and module 2 for impaired to disabled...have a good conversation, thank you. ")
        
        else :
                speak("good evening, welcome to the project vision. we are working on two different modals where we communicate with those persons who can not speak, listen, see the things. you have to select the module. please say module 1 for normal to impaired person and module 2 for impaired to disabled...have a good conversation, thank you. ")
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                speak("please speak......")
                r.pause_threshold = 0.8
                audio = r.listen(source)

        try:
                speak("recognizing.........")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said :{query}")
        


        except Exception as e:
                speak("please say that again...")
                return "none"
        return query
if __name__ == "__main__":
        wishMe()
        while True:
        #if 1: 
                query = takeCommand().lower()
                if 'module 1' in query:
                        speak("you have selected module one so i request you to speak load and clear in English Language")
                        mod1()
                        query = takeCommand().lower()
                        
               
                if 'module 2' in query:
                        speak("you have selected module two so i request you to create the hand gestures, you can see the output on screen")
                        mod2()
                        
                        
