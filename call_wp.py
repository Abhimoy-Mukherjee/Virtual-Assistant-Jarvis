# to make whatsapp call (vioce call)
import pyautogui
import time
import wp_chats

def calling(text):
    wp_chats.search(text)
    time.sleep(0.5)
    pyautogui.click(1351,56)
   # 1351 56