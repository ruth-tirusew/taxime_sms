from typing import Any, Dict, List
import httpx

from app.adapters import SMSAdapterInterface
from app.config import settings

class AfroSMSAdapter(SMSAdapterInterface):
    def __init__(self, identifier_id: str, auth_token: str):
        self.identifier_id = identifier_id
        self.auth_token = auth_token
        self.callback = "/callback"
        self.create_callback = "/createCallback"
        self.base_url = settings.AFROSMS_URL
    
    async def send_sms(self, phone: str, message: str) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/send",
                headers={
                    "Authorization": f"Bearer {self.auth_token}"
                },
                data={
                    'callback': self.callback,
                    'from':self.identifier_id,
                    'sender':settings.SENDER_NAME,
                    'to': phone,
                    'message': message
            })
            try:
                result =  response.json()
                print(result)
                if not result.get("acknowledge") == "success":
                    raise ValueError("Failed to send sms")
                return result.get("response")

            except Exception as jde:
                print(f"JSON decode error: {str(jde)} | Response text: {response.text}")
                raise jde
    
    async def send_bulk_sms(self, phone: List[str], message: str, campain_name:str) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/bulk_send",
                header={
                    "Authorization": f"Bearer {self.auth_token}"
                },
                data={
                    'from':self.identifier_id,
                    'sender':settings.SENDER_NAME,
                    'to': phone,
                    'message': message,
                    'createCallback':self.create_callback,
                    'statusCallback': self.callback,
            })
            return response.json()
    
    
    