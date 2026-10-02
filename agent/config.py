import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """ Gerenciador de configuração centralizado """
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    API_KEY_OMDB = os.getenv("API_KEY_OMDB")

    @classmethod
    def validate(cls):
        """ Valida se as variáveis de ambiente obrigatórias estão definidas. """

        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não esta definido no .env")
        
        elif not cls.API_KEY_OMDB:
                raise ValueError("API_KEY_OMDB não esta definido no .env")