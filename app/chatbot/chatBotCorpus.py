"""Import libraries """
import nltk
from nltk.chat.util import Chat, reflections

"""This is the corpus of the chat"""

my_pairs = [
  [
   r"(.*)hi|ola|hello|hola|buenas|buenos dias|buenas tardes(.*)",
   ["¡Hola! ¿En qué puedo colaborarte hoy?", "¡Hola! Bienvenido al servicio de asistencia de laboratorios UPTC. ¿En qué puedo ayudarte?"]
  ],
  [
    r"(.*) me llamo (.*)",
   ["¡Qué gusto conocerte, %l! ¿En qué puedo ayudarte?", "Un placer conocerte, %l. ¿En qué puedo colaborarte?"]
  ],
  [
   r"(.*)bien|muy bien|excelente|genial(.*)",
   ["Me alegra escucharlo. ¿En qué puedo asistirte hoy?", "¡Excelente! Estoy aquí para ayudarte. ¿En qué puedo colaborarte?"]
  ],
  [
    r"(.*)mal|regular|mas o menos|maso|horrible(.*)",
    ["Lamento escuchar eso. Cuéntame, ¿en qué puedo ayudarte a mejorar?", "No te preocupes, estoy aquí para ayudarte. ¿En qué puedo colaborarte?"]
  ],
  [
   r"(.*)te llamas|tu nombre(.*)",
   ["Me llamo Ramiro asistente virtual de Laboratorios UPTC. ¿En qué puedo colaborarte hoy?", "Puedes llamarme Ramiro asistente virtual de Laboratorios UPTC. ¿En qué puedo ayudarte?"]
  ],
  [
   r"(.*) como estas|estuvo tu dia|te ha ido ",
   ["Soy un asistente virtual, así que no tengo emociones, pero estoy aquí para ayudarte en lo que necesites. ¿En qué puedo colaborarte?", "Como asistente virtual, no tengo día ni emociones, pero siempre estoy listo para ayudar. ¿En qué puedo asistirte hoy?"]
  ],
  [
    r"(.*)de donde eres|donde naciste(.*)",
    ["Soy un asistente virtual creado para brindar asistencia en los laboratorios de la UPTC. ¿En qué puedo colaborarte hoy?", "No tengo lugar de nacimiento, fui desarrollado para ayudar en los laboratorios de la UPTC. ¿En qué puedo ayudarte?"]
  ],
  [
    r"(.*)que haces|estas haciendo|que tal(.*)",
    ["Estoy aquí para brindarte asistencia en los laboratorios de la UPTC. ¿En qué puedo colaborarte?", "Mi función es ayudarte con cualquier consulta relacionada con los laboratorios de la UPTC. ¿En qué puedo ayudarte hoy?"]
  ],
  [
   r"(.*)pregunta|duda|preguntar algo|consultar(.*)",
   ["Por supuesto, estoy aquí para responder tus preguntas. Adelante, cuéntame qué necesitas saber.", "Claro, puedes preguntarme lo que desees. Estoy aquí para ayudarte."]
  ],
  [
   r"(.*)gracias|muy amable|quit(.*)",
   ["De nada, estoy aquí para servirte. Si tienes más preguntas, no dudes en hacerlas.", "¡Gracias a ti! Si tienes más consultas, no dudes en preguntar. Estoy aquí para ayudarte."]
  ],
  [
  r"^(.*)(que|cuales) servicios (tiene|hay|ofrece) ?$"
   ["Puedo brindarte informacion acerca de los principales servicios que ofrecen los distintos laboratorios de la uptc a demás de sus tarifas, ubicacion y contacto.", "Yo te ofrezco informacion sobre los servicios que ofrecen los laboratorios de la uptc incluyendo tarifas, ubicacion y contacto."]
  ],
  [
    r"(.*)adios|hasta luego|nos vemos|chao|bye|vemos(.*)",
    ["Hasta luego, que tengas un excelente día.", "Nos vemos la próxima vez. ¡Que tengas un buen día!", "¡Hasta luego! Si tienes más consultas, no dudes en volver."]
]]


"""This method return the response of the chat with corpus"""
def chat(message):
  chat = Chat(my_pairs)
  response = chat.respond(message.lower())
  # Verificar si la respuesta es None o vacía
  if response is None or not response.strip():
      response = "Next"
    
  return response
