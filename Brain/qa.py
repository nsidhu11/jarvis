
import openai
from dotenv import load_dotenv

api_key = r"C:\Users\Navpreet Singh\Pictures\projects\jarvis\Database\api.txt"
fileopen = open(api_key, "r")
API = fileopen.read()
fileopen.close()

# API = "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"
logBook = r"C:\Users\Navpreet Singh\Pictures\projects\jarvis\Database\QA_log.txt"
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ques_ans(question, chat_log = None):
    with open(logBook,'r') as FileLog:
        chat_log_template = FileLog.read()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log} Question: {question}\nAnswer: '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion: {question} \nAnswer: {answer}"
    with open(logBook, 'w') as FileLog:
        FileLog.write(chat_log_template_update)
    return answer

print(brain_reply("What's date today"))