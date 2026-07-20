from fastapi import (
    APIRouter,
    Depends
)

from app.middleware.verify_token import (
    verify_token
)

router = APIRouter(
    prefix="/admin"
)

@router.get("/dashboard")

async def admin_dashboard(

    current_user: dict = Depends(
        verify_token
    )
):

    return {
        "message":
        "Welcome Admin",
        "user":
        current_user
    }