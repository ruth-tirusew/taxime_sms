from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config import settings, fastapi_config
from app.database import engine

app = FastAPI(**fastapi_config)

@app.on_event("shutdown")
def shutdown_db_client():
    engine.dispose()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
    allow_credentials=True,
)
