import os
from dotenv import load_dotenv

# Carregar variaveis do arquivo .env
load_dotenv()

class Config:
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    BASE_URL = "https://api.nasa.gov"