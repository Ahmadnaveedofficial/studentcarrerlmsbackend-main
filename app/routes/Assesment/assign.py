from fastapi import APIRouter
from app.config.db import assesment_collection
from app.models.AssesmentSchema import AssesmentModel
from app.controllers.Teacherassesment_controller import TeacherAssesmentController 


router = APIRouter(
    tags=["Assesment"]
)
@router.post("/create_assesment")
async def create_assesment(assesment: AssesmentModel):
    return  TeacherAssesmentController.create_assesment(assesment)

@router.get("/get_assesments/{classId}")
async def get_assesments(classId: str):
    return TeacherAssesmentController.get_assesments_by_teacher(classId)

@router.delete("/delete_assesment/{classId}")
async def delete_assesment(classId: str):
    return await TeacherAssesmentController.delete_assesment(classId)

@router.get("/all_assesments/{teacherId}")
async def all_assesments(teacherId: str):
    return await TeacherAssesmentController.all_assesments_get(teacherId)