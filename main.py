from fastapi import FastAPI
from app.services.chatbotService import formatResponse
from pydantic import BaseModel

app = FastAPI()

# from app.models import RequestChat
class RequestChat(BaseModel):
    message: str


@app.get('/')
def startChat():
    return {'message': "Hello World desde chatbot_api"}
@app.post('/')
def MakeChat(request: RequestChat):
    question = request.message 
    response = {
        'message': formatResponse(question)
    }
    return response

if __name__ == '__main__':
    app.run()