import pyautogui
import time

time.sleep(4)

count = 0

while count < 3:
    pyautogui.typewrite('I <3 U ')
    pyautogui.press('enter')
    count = count + 1
