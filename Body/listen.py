import speech_recognition as sr
from googletrans import Translator


# listen to user and take input for 5 seconds
# recognize the language of the input audio data 
# convert the audio input to text format in the language spoken by user
# return the text format of that audio input
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")
    except:
        return "Exception-thrown"

    query = str(query).lower()
    return query

# takes text input and convert that text input user desired language
# return converted language text
def translate_hindi_to_english(text):
    line = str(text)
    translator = Translator()
    result = translator.translate(text)
    data = result.text
    print(f"You: {data}.")
    return data


# call listen function for audio input and store that audio input in its original language in a variable
# call transate_hindi_to_english function to translate the hindi audio text to english
# return the translated text
def mic_execution():
    query = listen()
    data = translate_hindi_to_english(query)
    return data

