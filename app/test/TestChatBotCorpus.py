import unittest
import sys
sys.path.append('../chatbot')

from chatBotCorpus import chat


class TestChatBotCorpus(unittest.TestCase):
    def test_greeting(self):
        response = chat("Hola")
        self.assertIn(response, ["¡Hola! ¿En qué puedo colaborarte hoy?", "¡Hola! Bienvenido al servicio de asistencia de laboratorios UPTC. ¿En qué puedo ayudarte?"])

    def test_introduction(self):
        response = chat("Mi nombre es Juan")
        self.assertIn(response, ["Next"])

    def test_positive_feeling(self):
        response = chat("Muy bien")
        self.assertIn(response, ["Me alegra escucharlo. ¿En qué puedo asistirte hoy?", "¡Excelente! Estoy aquí para ayudarte. ¿En qué puedo colaborarte?"])

    def test_negative_feeling(self):
        response = chat("Horrible")
        self.assertIn(response, ["Lamento escuchar eso. Cuéntame, ¿en qué puedo ayudarte a mejorar?", "No te preocupes, estoy aquí para ayudarte. ¿En qué puedo colaborarte?"])

    def test_bot_name(self):
        response = chat("¿Cómo es tu nombre?")
        self.assertIn(response, ["Next"])

    def test_bot_status(self):
        response = chat("¿Cómo estás?")
        self.assertIn(response, ["Next"])

    def test_bot_origin(self):
        response = chat("¿De dónde eres?")
        self.assertIn(response, ["Next"])

    def test_bot_purpose(self):
        response = chat("¿Qué haces?")
        self.assertIn(response, ["Next"])

    def test_question(self):
        response = chat("Tengo una pregunta")
        self.assertIn(response, ["Por supuesto, estoy aquí para responder tus preguntas. Adelante, cuéntame qué necesitas saber.", "Claro, puedes preguntarme lo que desees. Estoy aquí para ayudarte."])

    def test_thanks(self):
        response = chat("Gracias")
        self.assertIn(response, ["De nada, estoy aquí para servirte. Si tienes más preguntas, no dudes en hacerlas.", "¡Gracias a ti! Si tienes más consultas, no dudes en preguntar. Estoy aquí para ayudarte."])

    def test_goodbye(self):
        response = chat("Adiós")
        self.assertIn(response, ["Hasta luego, que tengas un excelente día.", "Nos vemos la próxima vez. ¡Que tengas un buen día!", "¡Hasta luego! Si tienes más consultas, no dudes en volver."])

if __name__ == "__main__":
    unittest.main()
