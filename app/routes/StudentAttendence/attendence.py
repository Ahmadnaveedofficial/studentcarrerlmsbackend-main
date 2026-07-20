from fastapi import APIRouter
from app.controllers.studentAttendence_controller import StudentAttendenceController

router = APIRouter(
    tags=["Student Attendence"]
)

@router.get("/student-attendance/{student_id}/{classroom_id}")
async def get_student_attendance(student_id: str, classroom_id: str):
    return await StudentAttendenceController.get_student_attendance(
        student_id, classroom_id
    )
