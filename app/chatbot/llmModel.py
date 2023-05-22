from llama_index import LLMPredictor
from langchain.chat_models import ChatOpenAI

# Definir instacia del modelo
def generateModel():
    model = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'))
    return model