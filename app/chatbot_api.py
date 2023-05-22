from services.chatbotService import formatResponse
from chatBotCorpus import chat

while True:
    # response = chat()
    # if response is None:
    print("Entra en el modelo GPT")
    pregunta = input('Escribe tu pregunta \n') + "Responde en español"
    print(formatResponse(pregunta))




