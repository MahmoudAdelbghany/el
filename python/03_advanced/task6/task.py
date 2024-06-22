import pyautogui
import time
pyautogui.press('win')
time.sleep(1)
pyautogui.write('code')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
extensions = pyautogui.locateCenterOnScreen('extensions.png')
pyautogui.click(extensions)
time.sleep(1)


def install_extension(extension_name):
    # search_bar = pyautogui.locateCenterOnScreen('search_bar.png')
    # pyautogui.click(search_bar)
    # time.sleep(1)
    pyautogui.write(extension_name)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    install = pyautogui.locateCenterOnScreen('install.png')
    pyautogui.click(install)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    clear = pyautogui.locateCenterOnScreen('clear.png')
    pyautogui.click(clear)
    time.sleep(1)


extensions = ['clangd','c++ testmate','c++ helper','cmake','cmake tools']
for extension in extensions:
    install_extension(extension)
    time.sleep(5)
