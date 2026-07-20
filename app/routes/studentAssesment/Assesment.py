from fastapi import APIRouter
from app.controllers.student_Assesmnet_controller import Assesment

router = APIRouter(
    tags=["Student Assesment"]
)

@router.get("/student/assesments/{studentid}")
async def get_student_assesments(studentid: str):
    return Assesment.fetch_assement_by_student_userid(studentid)

@router.get("/student/assesment/{assesmentId}")
async def get_assesment_by_id(assesmentId: str):
    return await Assesment.get_assesment_by_id(assesmentId)