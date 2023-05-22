import os
from llama_index import GPTVectorStoreIndex, ServiceContext
from app.utilities import pdfManager
from app.chatbot  import llmModel
from decouple import config

# Carga de variables de sesion
OpenAiKey = config('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OpenAiKey
pdfs_path = config('DATA_PATH')


# Indexar el contenido de los PDF
pdfIndex = pdfManager.pdfDataReader(pdfs_path)
#index = GPTVectorStoreIndex.from_documents(pdfIndex)
service_context = ServiceContext.from_defaults(llm_predictor= llmModel.generateModel())
index = GPTVectorStoreIndex.from_documents(pdfIndex, service_context) 

# persistir index
#index.save_to_disk('index.json')

# # cargar index del disco
# index = GPTVectorStoreIndex.load_from_disk('index.json')
def makeQuestion(message):
    if len(pdfIndex) > 0 :
        query_engine = index.as_query_engine()
        response = query_engine.query(message)
        return response
    else: 
        exist= os.path.exists(pdfs_path)
        print(exist)
        print('no se ha cargado Data, ruta: ', os.getcwd())