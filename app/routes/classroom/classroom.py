from app.controllers.classroom_controller import classroomController
from fastapi import APIRouter
from app.models.classroomSchema import classroomModel
from app.models.studentSchema import StudentList
from app.config.db import classroom_collection, student_collection
from bson import ObjectId

router = APIRouter(
    tags=["Classroom"]
)

classroom_controller = classroomController
@router.post("/classroom_Added")
async def classroom_Added(classroom: classroomModel):
    return await classroom_controller.create_classroom(classroom)

@router.get("/classrooms")
async def classrooms():
    return await classroom_controller.fetch_classrooms()

@router.delete("/classroom/{id}")
async def delete_classroom(id: str):
    return await classroom_controller.delete_classroom(id)

@router.put("/classroom/{id}")
async def update_classroom(id: str, classroom: classroomModel):
    return await classroom_controller.update_classroom(id, classroom)

@router.get("/classroom/{id}")
async def classroom_detail(id: str):
    return await classroom_controller.classroom_detail(id)

@router.post("/classroom/{classroom_id}")
async def add_student_to_classroom(classroom_id: str, student: StudentList):
    return await classroom_controller.add_student(classroom_id, student)
