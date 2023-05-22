import textwrap
import sys
import os

dir_path= os.getcwd()
sys.path.append(dir_path)
print(sys.path) 

from app.chatbot import chatbotInstance

def formatResponse(question):
    res = chatbotInstance.makeQuestion(question)
    response = ''
    for frase in textwrap.wrap(res.response, width=100):
        response += frase + '\n'
    return response
