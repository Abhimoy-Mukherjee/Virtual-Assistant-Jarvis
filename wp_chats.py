# to open chats in whatsapp

import pyautogui
import time
import pyperclip
def search(text):
    n=1
    while (n==1):
      pyperclip.copy(text)
      #pyautogui.click(659,856)
      time.sleep(1)
      pyautogui.click(199,94)
      time.sleep(1)
      pyautogui.hotkey('command','v')
      time.sleep(1)
      pyautogui.press('enter')
      time.sleep(1)
      pyautogui.click(184,196)
      n+=1
    # 199 94
    # 184 196

