from fastapi import APIRouter
from app.config.db import attendence_collection
from app.controllers.TeacherAttendence_controller import TeacherAttendenceController
from app.models.AttendenceSchema import  AttendancePayload

router = APIRouter(
    tags=["Attendance"]
)
@router.post("/mark_attendance")
async def mark_attendance(data: AttendancePayload):
    return await TeacherAttendenceController.mark_attendance(data)