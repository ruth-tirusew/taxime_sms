from fastapi import Depends

from app.database import get_db
from app.modules.template.service import TemplateService
from app.modules.template.repository import TemplateRepository

def template_service_provider(db_session):
    repo = TemplateRepository(db_session)
    return TemplateService(repo)

def get_template_service(db=Depends(get_db)):
    return template_service_provider(db)
