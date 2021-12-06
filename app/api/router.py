from api import example, system
from fastapi.routing import APIRouter

api_router = APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(example.router, prefix="/example", tags=["example"])
