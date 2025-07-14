from pydantic import BaseModel, UUID4, Field
from typing import List


class TemplateBase(BaseModel):
    name: str
    messageTemplate: str


class GetTemplateModel(TemplateBase):
    id: UUID4

class GetAllTemplateModel(BaseModel):
    templates: List[GetTemplateModel]

class CreateTemplateModel(TemplateBase):
    ...

class UpdateTemplateModel(TemplateBase):
    ...
