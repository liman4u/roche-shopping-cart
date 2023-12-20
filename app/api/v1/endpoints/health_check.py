from fastapi import APIRouter

from app.core.settings import settings

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("/")
async def health_check_handler():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.API_VERSION,
        "status": "ok",
    }
