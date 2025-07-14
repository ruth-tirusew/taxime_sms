from pydantic import BaseModel, UUID4, Field
from typing import List


class TemplateBase(BaseModel):
    name: str
    messageTemplate: str


class CreateTemplateModel(TemplateBase):
    ...

class GetTemplateModel(TemplateBase):
    id: UUID4

class UpdateTemplateModel(TemplateBase):
    id: UUID4

class GetAllTemplateModel(TemplateBase):
    templates: List[GetTemplateModel]