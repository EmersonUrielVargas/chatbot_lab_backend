import textwrap

from chatbot import chatbotInstance

def formatResponse(question):
    res = chatbotInstance.makeQuestion(question)
    response = ''
    for frase in textwrap.wrap(res.response, width=100):
        response += frase + '\n'
    return response
