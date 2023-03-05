from tess import Ui_tessUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import sys
# import whatsapp


def speak(text):
    engine = pyttsx3.init("sapi5")  # sapi5: microsoft speech api for windows
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"You : {text}.")
    print("")
    engine.say(text)
    engine.runAndWait()


class main_Thread(QThread):

    def __init__(self):
        super(main_Thread, self).__init__()

    def run(self):
        self.Task_GUI()

    def take_command(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="hi")
            print(f"Your Command: {query}.\n")
        except:
            return "Exception-thrown"

        query = str(query).lower()
        return query

    def Task_GUI(self):
        speak("Welcome Navpreet.")
        while True:
            query = self.take_command()

            if "hello" in self.query:
                speak("Hello Sir, How are you?")
            elif "Whatsapp message" in query:
                query = query.replace("tess", "")
                query = query.replace("send", "")
                query = query.replace("whatsapp message", "")
                query = query.replace("to", "")
                name = query

                if "ripan" in self.name:
                    phone = "2369921717"
                    speak(f"What is the message for {name} ")
                    msg = self.take_command()
                    # whatsapp.whatsapp(phone, msg)


startFunction = main_Thread()


class Gui_Start(QMainWindow):

    def __init__(self):
        print("Testing.....")
        super().__init__()
        self.tess_ui = Ui_tessUI()
        self.tess_ui.setupUi(self)
        # self.tess_ui.label_3.clicked.connect(self.startFunc)
        # self.tess_ui.button.clicked.connect(self.close)

    def startFunc(self):
        print("5\n")
        self.tess_ui.movies_button = QtGui.QMovie("Siri_1.gif")
        self.tess_ui.button.setMovie(self.tess_ui.movies_button)
        self.tess_ui.movies_button.start()

        startFunction.start()
        print("6\n")


app_GUI = QApplication(sys.argv)
tess_GUI = Gui_Start()
tess_GUI.startFunc()
tess_GUI.show()
exit(app_GUI.exec_())
