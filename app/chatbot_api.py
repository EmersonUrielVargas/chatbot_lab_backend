from llama_index import GPTVectorStoreIndex, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import textwrap


import os
from decouple import config

OpenAiKey = config('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OpenAiKey

#Leer informacion de los PDF
pdfs_path = 'dataPDF'



# Definir instacia del modelo
def generateModel():
    model = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'))
    return model


# Indexar el contenido de los PDF
getpdfs = pdfDataload(pdfs_path)
index = GPTVectorStoreIndex.from_documents(getpdfs)
service_context = ServiceContext.from_defaults(llm_predictor=generateModel())
indexModel = GPTVectorStoreIndex.from_documents(pdfDataload(pdfs_path), service_context = service_context)

# persistir index
#index.save_to_disk('index.json')

# # cargar index del disco
# index = GPTVectorStoreIndex.load_from_disk('index.json')
if len(getpdfs) > 0 :
    while True:
        query_engine = index.as_query_engine()
        pregunta = input('Escribe tu pregunta \n') + "Responde en español"
        respuesta = query_engine.query(pregunta)
        for frase in textwrap .wrap(respuesta.response, width=100):
            print(frase)
else: 
    exist= os.path.exists(pdfs_path)
    print(exist)
    print('no se ha cargado Data, ruta: ', os.getcwd())


