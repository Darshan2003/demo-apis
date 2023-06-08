from fastapi import APIRouter
from src.endpoints import auth_endp

router = APIRouter()
router.include_router(auth_endp.router)


