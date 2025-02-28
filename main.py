import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import appLauncher
from weather import get_weather
import search_pyautogui
import wikipedia
import wp_chats
import call_wp

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif"open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
     elif"open youtube music" in c.lower():
          webbrowser.open("https://music.youtube.com/")
     elif"open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
     elif"open instagram" in c.lower():
          webbrowser.open("https://instagram.com")
    
     elif("song" in c.lower()):
          speak("Please tell me the name of the song")
          command = musicLibrary.listen_command()
          musicLibrary.play_song_from_youtube(command)
     elif("application" in c.lower()):
          speak("Please tell me the name of the application")
          audio=r.listen(source,timeout=2,phrase_time_limit=2)
          command=r.recognize_google(audio)
          appLauncher.open_app(command)
     elif("atmosphere" in c.lower()):
          speak("Which city's weather do you want to know? ")
          audio=r.listen(source,timeout=2,phrase_time_limit=2)
          city=r.recognize_google(audio)
          result=get_weather(city)
          speak(result)
     elif("search" and "google" in c.lower()):
         speak("what do you want me to search ")
         audio=r.listen(source,timeout=2,phrase_time_limit=2)
         search=r.recognize_google(audio)
         a=search_pyautogui.search(search)
     elif("search" and "wikipedia" in c.lower()):
         speak("what do you want me to search ")
         audio=r.listen(source,timeout=2,phrase_time_limit=2)
         search=r.recognize_google(audio)
         a=wikipedia.search(search)
     elif("call" in c.lower()):
          caller=(c.split()[-1])
          print(f"Calling {caller}....")
          appLauncher.open_app("whatsapp")
          call_wp.calling(caller)
     elif("whats" or "app" or "whatsapp" in (c.split()[-1])):
          speak("OK")
          of="of"
          chat=c.split()
          user=chat[chat.index(of)+1]
          appLauncher.open_app("whatsapp")
          wp_chats.search(user)

          
          
if __name__=="__main__":
    speak("Initializing  Jarvis....")
    while True:
        # listen for the wake word jarvis
        # obtain audio from microphone
        r=sr.Recognizer()
        print("Recognizing....\n")
        try:
            with sr.Microphone() as source:
                print("Listening....\n")
                audio=r.listen(source,timeout=2,phrase_time_limit=2)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                 speak("Yes")
                 # listen for command
                 with sr.Microphone() as source:
                     print("Jarvis Activated....")
                     audio=r.listen(source,timeout=2,phrase_time_limit=3)
                     command=r.recognize_google(audio)

                     processCommand(command)
        except Exception as e:
               print("Error ; {0}",format(e))
        if(word.lower()=="exit" or "terminate" in word.lower()):
            break
