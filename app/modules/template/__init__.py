from fastapi import APIRouter

from app.utils.route import import_routers

route = APIRouter(prefix="/templates", tags=["Templates"])
import_routers(__name__)
