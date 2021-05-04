#pip install pyautogui
import pyautogui
import time

i = 0
while i < 10:
    time.sleep(2)
    pyautogui.typewrite('# Everything fine friends?')
    pyautogui.press('enter')
    i += 1

    # Everything fine friends?
    # Everything fine friends?
    # Everything fine friends?
    # Everything fine friends?
    # Everything fine friends?
    # Everything fine friends?
    
