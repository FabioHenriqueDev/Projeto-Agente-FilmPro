from fastapi import APIRouter, HTTPException
from agent.models.movies import MovieRecommendation
from agent.models.request_model import RecommendationsResponse, RecomendationsRequest
from agent.core import recomendations

router = APIRouter()


@router.get(
    "/health",
    tags=["Sistema"],
    summary="Verificar saÃºde da API",
    description="Retorna o status da API"
)
async def health_check():
    """Endpoint simples para verificar se a API estÃ¡ online."""
    return {
        "status": "ok",
        "service": "FilmPro API",
        "version": "1.0.0"
    }


@router.post(
    '/recomendations',
    response_model=RecommendationsResponse,
    summary="Obter recomendaÃ§Ãµes de filmes",
    description="Gera recomendaÃ§Ãµes personalizadas de fillmes baseadas nas preferÃªncias do usuÃ¡rio",
    tags=["RecomendaÃ§Ãµes"]
)
async def get_recomendations(request: RecomendationsRequest) -> RecommendationsResponse:
    try:
        recomendation_resp: MovieRecommendation = await recomendations(preferences=request.preferences)
        
        if not recomendation_resp:
            raise HTTPException(status_code=500, detail="Erro ao gerar as recomendaÃ§Ãµes. Tente novamente")
        
        return RecommendationsResponse(
            sucess=True,
            data=recomendation_resp,
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao processar a rota: {e}')

