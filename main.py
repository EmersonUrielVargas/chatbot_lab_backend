from fastapi import FastAPI
from app.services.chatbotService import formatResponse
from pydantic import BaseModel

app = FastAPI()

# from app.models import RequestChat
class RequestChat(BaseModel):
    id: int
    message: str


@app.get('/')
def startChat():
    print('request entrada: ')
    return {'message': "Hello World desde chatbot_api"}
@app.post('/')
def MakeChat(request: RequestChat, response_model=None):
    question = request.message 
    return (formatResponse(question))