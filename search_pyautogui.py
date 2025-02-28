import pyautogui
import time
import webbrowser
import pyperclip
def search(text):
    n=1
    while (n==1):
      pyperclip.copy(text)
      webbrowser.open("https://google.com")
      #pyautogui.click(659,856)
      time.sleep(1)
      pyautogui.click(73,50)
   
      pyautogui.click(190,374)
      time.sleep(1)
      pyautogui.hotkey('command','v')
      time.sleep(1)
      pyautogui.press('enter')
      n+=1