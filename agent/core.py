import asyncio
from agent.models.movies import MovieRecommendation
from agent.prompts import *
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.websearch import WebSearchTools
from agent.config import Config
from agent.tools.omdb import search_movie


Config.validate()

# description → descreve quem/o que é o agente.
# instructions → dizem como ele deve se comportar/fazer o trabalho.

movie_recommendation_agent = Agent(
    name="FilmPro",
    model=OpenAIChat(id='gpt-4o', api_key=Config.OPENAI_API_KEY),
    description=description,
    instructions=instructions,
    add_datetime_to_context=True,
    tools=[WebSearchTools(backend="duckduckgo"), search_movie],
    output_schema=MovieRecommendation,
    debug_mode=True,
    debug_level=1
)

async def recomendations(preferences: str):
    result = await movie_recommendation_agent.arun(preferences, stream=False)

    if result and result.content:
        data: MovieRecommendation = result.content
        pretty_json_output = data.model_dump_json(indent=2)
        print(pretty_json_output)
        return data
    
    else:
        return None

 