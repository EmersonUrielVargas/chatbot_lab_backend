from app.chatbot import chatbotInstance
from app.chatbot.chatBotCorpus import chat

def formatResponse(question):
    print("La question es : " + question)
    res = chat(question)
    print("La respuesta es : " +  res)
    if res == 'Next':
        reqFormat = question + '\n Responde en español'
        print('El request format')
        print(reqFormat)
        response = chatbotInstance.makeQuestion(reqFormat).response
        return response
    else :
        return res
