from fastapi import APIRouter
from app.controllers.notifications_controller import NotificationController

router = APIRouter(prefix="/notifications", tags=["Notifications"])


# Teacher ke notifications fetch karna
@router.get("/teacher/{teacher_id}")
def get_teacher_notifications(teacher_id: str):

    return  NotificationController.get_teacher_notifications(teacher_id)