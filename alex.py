import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import pyautogui
import webbrowser
import cv2
import time
import sys
import operator
from hugchat import hugchat

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path=r"C:\Users\sabhya100\Desktop\Chatgpt\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
def openWebsite(query):
    if 'open' in query and 'website' in query:
      
        website_name = query.replace('open', '').replace('website', '').strip()
        
        if not website_name.startswith('http'):
            website_name = 'https://' + website_name +".com"
        
        webbrowser.open(website_name)
        speak(f"Opening {website_name}")
        print(f"Opening {website_name}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good Morning!")
        print("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Ready To Comply. What can I do for you ?")

def takeCommand():
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

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'hello alex' in query:
            print("hello sir")
            speak("hello sir")
        
        elif "time" in query:
            from datetime import datetime
            time = datetime.now().strftime("%H:%M")
            speak(f"The time now is : {time} ")
            print(f"The time now is : {time} ")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif "search in youtube" in query:
            pyautogui.click(x=800,y=130,clicks=1,interval=0,button='left')
        elif "search in google" in query:
            pyautogui.click(x=800,y=480,clicks=1,interval=0,button='left')
        elif "type" in query:  
            query=query.replace("type " ,"")
            pyautogui.typewrite(query)
            pyautogui.press("enter")
        elif "close this window" in query:
           pyautogui.click(x=1900,y=10,clicks=1,interval=0,button='left')
        elif "go back" in query:
           pyautogui.click(x=50,y=50,clicks=1,interval=0,button='left')
        elif "scroll down" in query:
            pyautogui.hscroll(-500,1) 
        elif "scroll up" in query:
            pyautogui.hscroll(500,1) 
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'close this tab' in query:
            pyautogui.hotkey('ctrl','w')
        elif 'open new tab' in query:
            pyautogui.hotkey('ctrl','t')
        elif 'open tab 1' in query:
            pyautogui.hotkey('ctrl','1')
        elif 'open tab 2' in query:
            pyautogui.hotkey('ctrl','2')
        elif 'open tab 3' in query:
            pyautogui.hotkey('ctrl','3')
        elif 'open tab 4' in query:
            pyautogui.hotkey('ctrl','4')
        elif 'open tab 5' in query:
            pyautogui.hotkey('ctrl','5')
        elif 'open previous tab' in query:
            pyautogui.hotkey('ctrl','9')
            
        elif 'open alliance' in query:
            webbrowser.open("https://www.alliance.edu.in")
        elif 'open presentation' in query:
            codePath = "C:\\Users\\sabhya100\\Desktop\\AI Voice assistant.pptx"
            os.startfile(codePath)
        elif 'open command' in query:
            os.system("start cmd.exe")
        elif 'close command' in query:
            os.system("taskkill /f /im cmd.exe") 
        elif 'first link' in query:
            pyautogui.click(x=450,y=250,clicks=1,interval=0,button='left')
        elif 'blank document' in query:
            pyautogui.click(x=500,y=200,clicks=1,interval=0,button='left')
        elif 'do not save' in query:
            pyautogui.click(x=980,y=570,clicks=1,interval=0,button='left')
        elif 'save' in query:
            pyautogui.click(x=900,y=570,clicks=1,interval=0,button='left')
        elif 'first video' in query:
            pyautogui.click(x=450,y=280,clicks=1,interval=0,button='left')
        elif 'second video' in query:
            pyautogui.click(x=450,y=520,clicks=1,interval=0,button='left')
        elif 'third video' in query:
            pyautogui.click(x=450,y=920,clicks=1,interval=0,button='left')
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('wwebcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "go to sleep" in query: 
            speak(' alright then, I am switching off') 
            sys.exit()
        elif "calculate" in query: 
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.adjust_for_ambient_noise (source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                }[op]
            def eval_bianary_expr (op1, oper, op2):
                op1, op2 = int(op1), int (op2)
                return get_operator_fn(oper) (op1, op2)
            result=(eval_bianary_expr(*(my_string.split())))
            print(f"Result: {result}") 
            speak("Your result is")
            speak(result)
               
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "unmute"  in query:
            pyautogui.press("volumemute")
        
        elif "open pc" in query:
            time.sleep(2)
            img = pyautogui.locateCenterOnScreen('ss1.png', confidence=0.3)
            pyautogui.doubleClick(img)
        elif "c drive" in query:
            pyautogui.click(x=650,y=200,clicks=2,interval=0,button='left')
        elif "d drive" in query:
            pyautogui.click(x=900,y=200,clicks=2,interval=0,button='left')
        elif "maximize this window" in query:
            pyautogui.hotkey('alt','space')
            pyautogui.press('x')
        elif "minimise this window" in query:
            pyautogui.hotkey('alt','space')
            pyautogui.press('n')
        elif "full" in query:
           pyautogui.click(x=800,y=500,clicks=1,interval=0,button='left')
        elif 'open' in query and 'website' in query:
            openWebsite(query)
        
        else:
            chatBot(query)