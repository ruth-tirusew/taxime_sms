from fastapi import HTTPException
from typing import Dict, Any, List

from app.modules.template.repository import TemplateRepository
from app.modules.template.schemas import (
    CreateTemplateModel,
    UpdateTemplateModel,
    GetAllTemplateModel,
    GetTemplateModel,
)

class TemplateService:
    def __init__(self, repository: TemplateRepository):
        self.repository = repository

    def _validate_template(self, name: str, message_template: str, template_id=None):
        if not name or not name.strip():
            raise HTTPException(status_code=400, detail="Template name must not be empty.")
        if not message_template or not message_template.strip():
            raise HTTPException(status_code=400, detail="Template messageTemplate must not be empty.")

        template = self.repository.get_template_by_name(name)
        if template and (not template_id or template.id != template_id):
            raise HTTPException(
                status_code=400, detail="Template with the given name already exists."
            )

    def create_template(self, template_data: CreateTemplateModel) -> GetTemplateModel:
        self._validate_template(template_data.name, template_data.messageTemplate)
        template = self.repository.create_template(template_data)
        return GetTemplateModel.model_validate(template)

    def update_template(self, template_id, update_data: UpdateTemplateModel) -> GetTemplateModel:
        self._validate_template(update_data.name, update_data.messageTemplate, template_id=template_id)
        template = self.repository.update_template(template_id, update_data)
        return GetTemplateModel.model_validate(template.__dict__)

    def get_template_by_id(self, template_id) -> GetTemplateModel:
        template = self.repository.get_template_by_id(template_id)
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        return GetTemplateModel.model_validate(template.__dict__)

    def get_all_templates(self) -> GetAllTemplateModel:
        templates = self.repository.get_all_templates()
        return GetAllTemplateModel(templates=[GetTemplateModel.model_validate(t.__dict__) for t in templates])

    def delete_template(self, template_id):
        template = self.repository.get_template_by_id(template_id)
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        self.repository.delete_template(template_id)
        return {"detail": "Template deleted"}

    def get_template_by_name(self, name: str) -> GetTemplateModel:
        template = self.repository.get_template_by_name(name)
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        return GetTemplateModel.model_validate(template)