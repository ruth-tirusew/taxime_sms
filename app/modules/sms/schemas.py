from pydantic import BaseModel, UUID4, Field, Optional
from typing import List


phone_regex = r'^\+?[1-9]\d{1,14}$'


class SMSBase(BaseModel):
    phone: str = Field(..., regex=phone_regex)
    message: Optional[str]=None
    template_id: Optional[UUID4]=None



class CreateSMS(SMSBase):
    ...

class GetSMS(SMSBase):
    id: UUID4

class GetAllSMS(BaseModel):
    sms: List[GetSMS]

