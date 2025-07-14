from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config import settings, fastapi_config
from app.database import Base, engine, get_db
from app.dependencies import get_container

from app.modules.sms import route as sms_router
from app.modules.template import route as template_router

from app.modules.sms.provider import get_sms_service, sms_service_provider
from app.modules.template.provider import get_template_service, template_service_provider

from app.sms import get_sms_adapter


container = get_container()
container.register("template_service", lambda: template_service_provider(next(get_db())))
container.register("sms_service", lambda: sms_service_provider(next(get_db()), container.resolve("template_service"), get_sms_adapter()))


app = FastAPI(**fastapi_config)

Base.metadata.create_all(bind=engine)

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

app.include_router(sms_router)
app.include_router(template_router)

