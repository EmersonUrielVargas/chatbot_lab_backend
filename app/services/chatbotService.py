from app.chatbot import chatbotInstance
from app.chatbot.chatBotCorpus import chat
from app.chatbot.chatBotCorpusRive import generateMessage

def formatResponse(question):
    print("La question es : " + question)
    response = chat(question)
    print("La respuesta es : " +  res)
    if response == 'Next':
        reqFormat = question + '\n Responde en español'
        print('El request format')
        print(reqFormat)
        response = chatbotInstance.makeQuestion(reqFormat).response
    return response
