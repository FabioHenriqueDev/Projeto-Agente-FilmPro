from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .routers import router

SITE_DIR = Path(__file__).resolve().parent.parent / "site"

app = FastAPI(
    title="FilmPro API",
    description="API de recomendação inteligente de filmes usando IA",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def serve_site():
    return FileResponse(SITE_DIR / "index.html")


app.include_router(router)
app.mount("/", StaticFiles(directory=SITE_DIR), name="site")
