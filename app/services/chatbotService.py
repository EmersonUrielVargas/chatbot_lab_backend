from app.chatbot import chatbotInstance

def formatResponse(question):
    reqFormat = question + '\n Responde en español'
    return chatbotInstance.makeQuestion(reqFormat).response
