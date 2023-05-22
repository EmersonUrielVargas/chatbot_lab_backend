import unittest
from unittest.mock import patch
import sys
sys.path.append('../chatbot')
from chatbotInstance import makeQuestion

class TestChatbootInstance(unittest.TestCase):

    def test_makeQuestion_with_pdfIndex(self):
        # Arrange
        pdfIndex = ['pdf1', 'pdf2', 'pdf3']
        expected_response = 'Response'

        # Act
        with patch('chatbootInstance.index.as_query_engine') as mock_query_engine:
            mock_query_engine.return_value.query.return_value = expected_response
            response = makeQuestion('question', pdfIndex)

        # Assert
        self.assertEqual(response, expected_response)

    def test_makeQuestion_without_pdfIndex(self):
        # Arrange
        pdfIndex = []
        expected_response = 'no se ha cargado Data, ruta: /current/working/directory'

        # Act
        with patch('chatbootInstance.os.path.exists') as mock_exists:
            mock_exists.return_value = False
            with patch('chatbootInstance.os.getcwd') as mock_getcwd:
                mock_getcwd.return_value = '/current/working/directory'
                response = makeQuestion('question', pdfIndex)

        # Assert
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
