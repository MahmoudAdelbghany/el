import pyautogui
import time
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite('edge') 
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('https://mail.google.com')
pyautogui.press('enter')

time.sleep(5)

pyautogui.moveTo(x=500, y=350)
pyautogui.click()

time.sleep(2)

pyautogui.hotkey('alt', 'left')

pyautogui.moveTo(x=500, y=400)
pyautogui.click()

time.sleep(2)

pyautogui.hotkey('alt', 'left')

pyautogui.moveTo(x=500, y=450)
pyautogui.click()

time.sleep(2)

pyautogui.hotkey('ctrl', 'w')