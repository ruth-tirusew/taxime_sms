from typing import Dict, Any
from app.adapters import SMSAdapterInterface, CacheAdapterInterface
from app.modules.sms.repository import SMSRepository
from app.modules.sms.schemas import SMSCreate, SMSResponse
from app.modules.template.service import TemplateService

class SMSService:
    def __init__(
        self,
        sms_adapter: SMSAdapterInterface,
        template_service: TemplateService
        repository: SMSRepository
    ):
        self.sms_adapter = sms_adapter
        self.repository = repository

    async def create_sms(self, sms_data: SMSCreate) -> Dict[str, Any]:
        message = sms_data.message
        if sms_data.template_id:
            template = self.template_service.get_template_by_id(sms_data.template_id)
            if not template:
                raise ValueError("Template not found.")
            message = template.messageTemplate
        elif not message or not message.strip():
            raise ValueError("Either message or template_id must be provided.")
        send_result = await self.sms_adapter.send_sms(sms_data.phone, message)
        sms_record = self.repository.create_sms(sms_data, send_result.get("message_id"))
        return {"send_result": send_result, "sms_record": sms_record}

    def get_sms_by_id(self, sms_id):
        return self.repository.get_sms_by_id(sms_id)

    def get_all_sms(self):
        return self.repository.get_all_sms()

    def update_sms(self, sms_id, update_data):
        return self.repository.update_sms(sms_id, update_data)

    def delete_sms(self, sms_id):
        return self.repository.delete_sms(sms_id)

    async def send_bulk_sms(self, phones: list, message: str) -> Dict[str, Any]:
        return await self.sms_adapter.send_bulk_sms(phones, message)