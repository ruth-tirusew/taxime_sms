from fastapi import Depends

from app.adapters import SMSAdapterInterface
from app.database import get_db
from app.modules.sms.service import SMSService
from app.modules.sms.repository import SMSRepository

from app.modules.template.service import TemplateService

def sms_service_provider(db_session, template_service: TemplateService, sms_adapter: SMSAdapterInterface):
    repo = SMSRepository(db_session)
    return SMSService(sms_adapter=sms_adapter, template_service=template_service, repository=repo)

def get_sms_service(db=Depends(get_db)):
    return sms_service_provider(db)
