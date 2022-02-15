from fastapi import APIRouter
from .user import router as user_router
from .private import router as private_router

router = APIRouter()
router.include_router(user_router)
router.include_router(private_router)
