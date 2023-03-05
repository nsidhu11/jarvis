import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


# Using in built window based voices for to text to speech
# window based is fast, offline source but do have many option for voices
# no over-speaking(i.e. can not listen while answering) allowed in window based
# -----------------------------------------------------------------------------------
# def speak(text):
#     engine = pyttsx3.init("sapi5")  # sapi5: microsoft speech api for windows
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[0].id)
#     engine.setProperty('rate', 170)
#     print("")
#     print(f"You : {text}.")
#     print("")
#     engine.say(text)
#     engine.runAndWait()
# -----------------------------------------------------------------------------------------


# download Chrome web driver from https://chromedriver.chromium.org/downloads
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "Database/chromedriver.exe"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')


def speak(text):
    length_of_text = len(str(text))
    if length_of_text == 0:
        pass
    else:
        print("")
        print(f"AI: {text}.")
        print("")
        data = str(text)
        x_path_of_sec = '/html/body/div[4]/div[2]/form/textarea'
        value_id = '//*[@id="vorlesenbutton"]'

        driver.find_element(By.XPATH, value=x_path_of_sec).send_keys(data)
        driver.find_element(By.XPATH, value=value_id).click()
        driver.find_element(By.XPATH, value=x_path_of_sec).clear()

        if length_of_text >= 30:
            sleep(4)
        elif length_of_text >= 40:
            sleep(6)
        elif length_of_text >= 55:
            sleep(15)
        elif length_of_text >= 70:
            sleep(10)
        elif length_of_text >= 100:
            sleep(13)
        elif length_of_text >= 120:
            sleep(14)
        else:
            sleep(2)

