from fastapi import APIRouter, HTTPException, status
from app.dependencies import get_container
from app.modules.template.schemas import CreateTemplateModel, UpdateTemplateModel, GetAllTemplateModel

from . import route

def get_template_service_from_container():
    return get_container().resolve("template_service")

@route.get("/", response_model=GetAllTemplateModel)
def list_templates():
    template_service = get_template_service_from_container()
    templates = template_service.get_all_templates()
    return templates

@route.get("/{template_id}")
def get_template(template_id: str):
    template_service = get_template_service_from_container()
    template = template_service.get_template_by_id(template_id)
    if not template:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Template not found")
    return template

@route.post("/", status_code=status.HTTP_201_CREATED)
def create_template(template_data: CreateTemplateModel):
    template_service = get_template_service_from_container()
    return template_service.create_template(template_data)

@route.put("/{template_id}")
def update_template(template_id: str, update_data: UpdateTemplateModel):
    template_service = get_template_service_from_container()
    return template_service.update_template(template_id, update_data)

@route.delete("/{template_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_template(template_id: str):
    template_service = get_template_service_from_container()
    template_service.delete_template(template_id)
    return None
