from fastapi import APIRouter, HTTPException, status
from app.dependencies import get_container
from app.modules.sms.schemas import CreateSMS, UpdateSMS, GetAllSMS

from . import route

def get_sms_service_from_container():
    return get_container().resolve("sms_service")

@route.get("/", response_model=GetAllSMS)
def list_sms():
    sms_service = get_sms_service_from_container()
    sms = sms_service.get_all_sms()
    return sms

@route.get("/{sms_id}")
def get_sms(sms_id: str):
    sms_service = get_sms_service_from_container()
    sms = sms_service.get_sms_by_id(sms_id)
    if not sms:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Template not found")
    return sms

@route.post("/", status_code=status.HTTP_201_CREATED)
async def create_sms(sms_data: CreateSMS):
    sms_service = get_sms_service_from_container()
    print("Request_____", sms_data)
    return await sms_service.create_sms(sms_data)

@route.put("/{sms_id}")
def update_sms(sms_id: str, update_data: UpdateSMS):
    sms_service = get_sms_service_from_container()
    return sms_service.update_sms(sms_id, update_data)

@route.delete("/{sms_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sms(sms_id: str):
    sms_service = get_sms_service_from_container()
    sms_service.delete_sms(sms_id)
    return None
