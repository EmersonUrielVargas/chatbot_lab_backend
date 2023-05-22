from services.chatbotService import formatResponse

while True:
    pregunta = input('Escribe tu pregunta \n') + "Responde en español"
    print(formatResponse(pregunta))



