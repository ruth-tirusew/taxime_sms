import uuid
from datetime import datetime
from typing import Optional, List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.modules.template.models import TemplateModel
from app.modules.template.schemas  import CreateTemplateModel


class TemplateRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_template(self, template_data: CreateTemplateModel) -> TemplateModel:
        template = TemplateModel(**template_data.dict())
        self.db.add(template)
        try:
            self.db.commit()
            self.db.refresh(template)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Template creation failed due to integrity error.")
        return template

    def get_template_by_id(self, template_id) -> Optional[TemplateModel]:
        uuid_obj = uuid.UUID(template_id)
        return self.db.query(TemplateModel).filter(TemplateModel.id == uuid_obj).first()

    
    def get_template_by_name(self, name: str) -> Optional[TemplateModel]:
        return self.db.query(TemplateModel).filter(TemplateModel.name == name).first()
   

    def get_all_templates(self) -> List[TemplateModel]:
        return self.db.query(TemplateModel).all()

    def update_template(self, template_id, update_data) -> TemplateModel:
        template = self.get_template_by_id(template_id)
        if not template:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Template not found.")
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(template, field, value)
        try:
            self.db.commit()
            self.db.refresh(template)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Template update failed due to integrity error.")
        return template

    def delete_template(self, template_id) -> None:
        template = self.get_template_by_id(template_id)
        if not template:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Template not found.")
        self.db.delete(template)
        self.db.commit()
