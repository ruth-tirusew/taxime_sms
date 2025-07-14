from typing import Dict, Any
from app.adapters import SMSAdapterInterface, CacheAdapterInterface
from app.modules.template.repository import TemplateRepository

class TemplateService:
    def __init__(
        self,
        repository: TemplateRepository
    ):
        self.repository = repository

    def _validate_template(self, name: str, message_template: str, template_id=None):
        if not name or not name.strip():
            raise ValueError("Template name must not be empty.")
        if not message_template or not message_template.strip():
            raise ValueError("Template messageTemplate must not be empty.")

        template = self.repository.get_template_by_name(name)
        if template:
            raise ValueError("Template with the given name already exists.")
        
    def create_template(self, template_data):
        self._validate_template(template_data.name, template_data.messageTemplate)
        return self.repository.create_template(template_data)

    def update_template(self, template_id, update_data):
        self._validate_template(update_data.name, update_data.messageTemplate, template_id=template_id)
        return self.repository.update_template(template_id, update_data)

    def get_template_by_id(self, template_id):
        return self.repository.get_template_by_id(template_id)

    def get_all_templates(self):
        return self.repository.get_all_templates()

    def delete_template(self, template_id):
        return self.repository.delete_template(template_id)

    def get_template_by_name(self, name: str):
        return self.repository.get_template_by_name(name)