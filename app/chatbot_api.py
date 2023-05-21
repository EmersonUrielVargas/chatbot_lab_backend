import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import textwrap
from decouple import config

#Leer informacion de los PDF
pdfs_path = 'dataPDF'
pdf = SimpleDirectoryReader(pdfs_path).load_data()

#obtenemos el api_key de openAI
OpenAiKey = config('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OpenAiKey

#Leer informacion de los PDF
pdfs_path = 'dataPDF'
pdf = SimpleDirectoryReader(pdfs_path).load_data()

# Definir instacia del modelo
model = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo-0301'))

# Indexar el contenido de los PDF
service_context = ServiceContext.from_defaults(llm_predictor=model)
index = GPTVectorStoreIndex.from_documents(pdf, service_context = service_context)

# #persistir index
index.save_to_disk('index.json')

# cargar index del disco
index = GPTVectorStoreIndex.load_from_disk('index.json')

while True:
    query_engine = index.as_query_engine()
    pregunta = input('Escribe tu pregunta \n') + "Responde en español"
    respuesta = query_engine.query(pregunta)
    for frase in textwrap .wrap(respuesta.response, width=100):
        print(frase)


