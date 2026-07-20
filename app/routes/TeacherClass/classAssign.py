from fastapi import APIRouter
from app.controllers.TeacherClassController import TeacherClassController
router = APIRouter(
    tags=["TeacherClass"]
)
teacher_class_controller = TeacherClassController()
@router.get("/classes/assigned/{teacher_id}")
async def get_assigned_classes(teacher_id: str):
    return teacher_class_controller.show_classes_to_assign_teacher(teacher_id)