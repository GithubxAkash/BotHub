# Working Bot

import os
import time
import webbrowser
import pyautogui

url = "https://www.youtube.com/watch?v=SYi3NeaAhuw&autoplay=1&mute=1"
num_iterations = 20

for i in range(num_iterations):
    webbrowser.open(url)
    time.sleep(5)  # Wait for 5 seconds
    pyautogui.press("f")  # Enter full screen mode
    time.sleep(1)  # Wait for 1 second
    pyautogui.press("f")  # Exit full screen mode
    time.sleep(15)  # Wait for 1 minute (or adjust as necessary)
    pyautogui.hotkey("ctrl", "w")  # Close tab
    time.sleep(5)  # Wait for 5 seconds before opening the next URL
    os.system("TASKKILL /F /IM chrome.exe")