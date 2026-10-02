from pydantic import BaseModel, Field
from agent.models.movies import MovieRecommendation

class RecomendationsRequest(BaseModel):
    preferences: str = Field(
        description="",
        min_length=10,
        max_length=500
    )


class RecommendationsResponse(BaseModel):
    sucess: bool = Field(..., description="Indica se a recomendação foi bem sucedida")
    data: MovieRecommendation = Field(..., description="Dados das recomendações")
    message: str = Field(default="Recomendações geradas com sucesso", description="mensagem informativa")