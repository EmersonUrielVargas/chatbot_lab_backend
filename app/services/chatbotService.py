from app.chatbot import chatbotInstance
from app.chatbot.chatBotCorpus import chat

def formatResponse(question):
    response = chat()
    if response is None:
        reqFormat = question + '\n Responde en español'
        response = chatbotInstance.makeQuestion(reqFormat).response
    return response
