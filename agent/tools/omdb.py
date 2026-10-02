import os
from typing import Any
from dotenv import load_dotenv
import aiohttp
from agent.config import Config

Config.validate()

async def search_movie(title: str) -> dict[str, Any] | str:

    """
        Pesquisa informações de um filme pelo título.
        Retorna informações como elenco, diretor, ano,
        gênero, duração, avaliação, poster e etc.
    """
    api_key = Config.API_KEY_OMDB

    if not api_key:
        raise ValueError("API_KEY_OMDB não foi configurada")


    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                "http://www.omdbapi.com/",
                params={
                    "apikey": api_key,
                    "t": title,   
                    "type": "movie",
                    "plot": "full",  # Enredo completoo
                    "v": "1"  # versão da API
                },
                timeout=aiohttp.ClientTimeout(total=10) # timeout de 10 segundos se na oretorna nada em 10 gera erro
            ) as response:
                if response.status != 200:
                    return f"Erro ao buscar filme Status {response.status}"
                else:
                    result = await response.json()
                    
                    if result.get("Response") == "False":
                        return f'Filme não encontrado: {title}'

                    return result
        except Exception as e:
            return f'Erro na busca do filme: {e}'




    
