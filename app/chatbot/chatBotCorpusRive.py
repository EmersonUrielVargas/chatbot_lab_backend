#importacion de librerias
from rivescript import RiveScript

#Inicializamos rivescript y cargamos corpus
bot = RiveScript()
bot.load_file("app/chatbot/content/corpus.rive")
bot.sort_replies()

#Se genera la respuesta al mensaje de usuario
def generateMessage(message):
    response= bot.reply('local', msg=message)
    return response
