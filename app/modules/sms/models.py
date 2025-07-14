from app.models.base import BaseModel
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

class SMSModel(BaseModel):
    __tablename__="sms"
    
    phone = Column(String(20), nullable=False)
    message = Column(Text)
    template_id = Column(UUID(as_uuid=True), ForeignKey('templates.id'), nullable=True)
    message_id = Column(String(255))

    template = relationship("TemplateModel", back_populates="sms_messages")

