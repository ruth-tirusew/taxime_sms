from typing import Optional, List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.modules.sms.models import SMSModel

class SMSRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_sms(self, sms_data, message_id) -> SMSModel:
        sms = SMSModel({**sms_data.dict(), "message_id": message_id})
        self.db.add(sms)
        try:
            self.db.commit()
            self.db.refresh(sms)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SMS creation failed due to integrity error.")
        return sms

    def get_sms_by_id(self, sms_id) -> Optional[SMSModel]:
        return self.db.query(SMSModel).filter(SMSModel.id == sms_id).first()

    def get_all_sms(self) -> List[SMSModel]:
        sms =  self.db.query(SMSModel).all()
        print(sms)
        return sms

    def update_sms(self, sms_id, update_data) -> SMSModel:
        sms = self.get_sms_by_id(sms_id)
        if not sms:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SMS not found.")
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(sms, field, value)
        try:
            self.db.commit()
            self.db.refresh(sms)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SMS update failed due to integrity error.")
        return sms

    def delete_sms(self, sms_id) -> None:
        sms = self.get_sms_by_id(sms_id)
        if not sms:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SMS not found.")
        self.db.delete(sms)
        self.db.commit()

    def get_sms_by_phone(self, phone: str) -> List[SMSModel]:
        return self.db.query(SMSModel).filter(SMSModel.phone == phone).all()

    def get_sms_by_template_id(self, template_id) -> List[SMSModel]:
        return self.db.query(SMSModel).filter(SMSModel.template_id == template_id).all()
