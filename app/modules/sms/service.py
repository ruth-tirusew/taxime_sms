from typing import Dict, Any
from app.adapters import SMSAdapterInterface, CacheAdapterInterface
from app.modules.sms.repository import SMSRepository
from app.modules.sms.schemas import SMSCreate, SMSResponse

class SMSService:
    def __init__(
        self,
        sms_adapter: SMSAdapterInterface,
        repository: SMSRepository
    ):
        self.sms_adapter = sms_adapter
        self.repository = repository