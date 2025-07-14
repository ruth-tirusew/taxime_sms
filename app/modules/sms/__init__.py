from fastapi import APIRouter

from app.utils.route import import_routers

route = APIRouter(prefix="/sms", tags=["SMS"])
import_routers(__name__)
