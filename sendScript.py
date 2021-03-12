import time
import pyautogui

def SendScipt():
  time.sleep(2)
  with open('script.txt') as f:
    lines = f.readlines()
  for line in lines:
    pyautogui.typewrite(line.strip())
    pyautogui.press('enter')

print("running")
SendScipt()
