from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from llama_index import download_loader
from langchain.chat_models import ChatOpenAI
import textwrap


import os
from decouple import config

OpenAiKey = config('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OpenAiKey

#Leer informacion de los PDF
pdfs_path = 'dataPDF'
def pdfDataload(path):
    pdf = SimpleDirectoryReader(path).load_data()
    print(pdf)
    return pdf


# Definir instacia del modelo
def generateModel():
    model = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'))
    return model


# Indexar el contenido de los PDF
index = GPTVectorStoreIndex.from_documents(pdfDataload(pdfs_path))
service_context = ServiceContext.from_defaults(llm_predictor=generateModel())
indexModel = GPTVectorStoreIndex.from_documents(pdfDataload(pdfs_path), service_context = service_context)

# persistir index
#index.save_to_disk('index.json')

# # cargar index del disco
# index = GPTVectorStoreIndex.load_from_disk('index.json')

while True:
    query_engine = index.as_query_engine()
    pregunta = input('Escribe tu pregunta \n') + "Responde en español"
    respuesta = query_engine.query(pregunta)
    for frase in textwrap .wrap(respuesta.response, width=100):
        print(frase)


