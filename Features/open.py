import os
import keyboard
import pyautogui
import webbrowser
from time import  sleep

def open_exec(query):
    query = str(query).lower()

    if "visit" in query:
        website_name = query.replace("visit", "")
        if " " in website_name:
            website_name = website_name.replace(" ", "")
        link = f"https://www.{website_name}.com"
        webbrowser.open(link)

    elif "open" in query or "start" in query:
        application_name = query.replace("open", "")
        if " " in application_name:
            website_name = application_name.replace(" ", "")
        # if "chrome" in application_name:
        #     os.startfile(r"path_to_chrome.exe_file")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(application_name)
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        return True
