from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

class SMSAdapterInterface(ABC):
    @abstractmethod
    async def send_sms(self, phone: str, message: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def send_bulk_sms(self, phone: List[str], message: str) -> Dict[str, Any]:
        pass

    async def send_personalized_bulk_sms(self, phone):
        pass
    
    async def callback(self, message_id:str) ->Dict[str, Any]:
        pass

class CacheAdapterInterface(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        pass
    
    @abstractmethod
    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        pass
    
    @abstractmethod
    async def delete(self, key: str) -> bool:
        pass