from Brain.brainAI import brain_reply
from Brain.qa import ques_ans
from Body.listen import mic_execution
from Body.speak import speak
from Features.clap import Tester
from main import main_task_execution

print("\nStarting your personal AI chatbot.Wait for few seconds...")

def main_execution():
    speak("Hello Nav")
    speak("My name is TESS. I welcome you to your personal AI chatbot")
    speak("How can I help you?")

    while True:
        Data = mic_execution()
        Data = str(Data)
        return_value = main_task_execution(Data)
        if return_value:
            pass
        elif len(Data) < 3:
            pass
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data or "How" in Data :
            Reply = ques_ans(Data)
            speak(Reply)
        else:
            Reply = brain_reply(Data)
            speak(Reply)


def clap_detection():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        main_execution()
    else:
        pass


main_execution()