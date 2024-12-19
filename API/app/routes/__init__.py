from fastapi import APIRouter
from .associate_router import router as associate_router
from .dependent_router import router as dependent_router
from .donations_router import router as donations_router
from .orphanages_router import router as orphanages_router
main_router = APIRouter()
main_router.include_router(associate_router)
main_router.include_router(dependent_router)
main_router.include_router(donations_router)
main_router.include_router(orphanages_router)