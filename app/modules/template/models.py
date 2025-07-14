from app.models.base import BaseModel
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

class TemplateModel(BaseModel):
    __tablename__ = "templates"
    name = Column(String(255), nullable=False)
    messageTemplate = Column(Text, nullable=False)
    
    sms_messages = relationship("SMSModel", back_populates="template")

