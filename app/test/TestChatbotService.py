import unittest
import sys
sys.path.append('../services')
from chatbotService import formatResponse

class TestChatbotService(unittest.TestCase):
    def test_formatResponse(self):
        # Caso de prueba 1: pregunta con respuesta directa
        question = "¿Cuál es tu nombre?"
        expected_response = "Mi nombre es Chatbot"
        actual_response = formatResponse(question)
        self.assertEqual(actual_response, expected_response)

        # Caso de prueba 2: pregunta con respuesta "Next"
        question = "Siguiente pregunta"
        expected_response = "Respuesta en español"
        actual_response = formatResponse(question)
        self.assertEqual(actual_response, expected_response)

        # Caso de prueba 3: pregunta con respuesta "Next" que genera otra pregunta
        question = "Siguiente pregunta"
        expected_response = "Respuesta generada por chatbotInstance"
        actual_response = formatResponse(question)
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
