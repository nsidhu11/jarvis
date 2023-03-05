# # import pyttsx3
# #
# # # Create a text-to-speech engine
# # engine = pyttsx3.init()
# #
# # # Set the voice properties
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[0].id) # Change the index to change the voice
# #
# # # Convert text to speech
# # text = "Hello, World!"
# # engine.say(text)
# # engine.runAndWait()
#
# from gtts import gTTS
# import os
# import threading
# import time
#
# class SpeechThread(threading.Thread):
#     def __init__(self, text, language='en', voice=None):
#         threading.Thread.__init__(self)
#         self.text = text
#         self.language = language
#         self.voice = voice
#
#     def run(self):
#         tts = gTTS(text=self.text, lang=self.language, slow=False, lang_check=True)
#
#         # Save speech to temporary file
#         tts_file = 'speech.mp3'
#         tts.save(tts_file)
#
#         # Play speech file and delete temporary file when finished
#         os.system(f"start {tts_file} && (ping 127.0.0.1 -n 2 > nul) && del {tts_file}")
#
# def speak(text):
#     length_of_text = len(str(text))
#     if length_of_text == 0:
#         pass
#     else:
#         print("")
#         print(f"AI: {text}.")
#         print("")
#
#         speech_thread = SpeechThread(text)
#         speech_thread.start()
#
#         # Determine sleep time based on length of text
#         if length_of_text >= 30:
#             time.sleep(60)
#         elif length_of_text >= 40:
#             time.sleep(60)
#         elif length_of_text >= 55:
#             time.sleep(60)
#         elif length_of_text >= 70:
#             time.sleep(60)
#         elif length_of_text >= 100:
#             time.sleep(63)
#         elif length_of_text >= 120:
#             time.sleep(64)
#         else:
#             time.sleep(3)
#
# speak("Hello Navpreet Singh Sidhu")
# speak("Hello Ripanjeet Singh Sidhu")
# speak("Hello Amandeep Kaur Sandhu")


import pyttsx3


def speak(text):
    # initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # initialize the overspeak list
    overspeak_list = []

    # define a function to handle the speech start event
    def on_start(name):
        print('Starting to speak...')

    # define a function to handle the speech end event
    def on_end(name, completed):
        print('Finished speaking.')

        # if there is overspeak input, speak it next
        if overspeak_list:
            next_input = overspeak_list.pop(0)
            speak(next_input)

    # set the event handlers on the engine
    engine.connect('started-utterance', on_start)
    engine.connect('finished-utterance', on_end)

    # set the text to be spoken
    engine.say(text)

    # start the speech
    engine.runAndWait()

    # if there is overspeak input left, speak it next
    if overspeak_list:
        next_input = overspeak_list.pop(0)
        speak(next_input)


# example usage
# speak('Hello, how are you today?')
# speak('Please enter your name:')
# name = input()
# speak('Nice to meet you, ' + name + '!')

print(len(" My name is TESS. I welcome you to your personal AI chatbot.."))