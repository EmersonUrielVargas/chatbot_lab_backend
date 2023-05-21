import os
from decouple import config

OpenAiKey = config('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OpenAiKey