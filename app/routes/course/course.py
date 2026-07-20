from fastapi import APIRouter
from app.controllers.course_controller import courseController
from app.models.TeacherSchema import courseModel

router = APIRouter(
    prefix="/teacher/course",
    tags=["Teacher Courses"]
)

course_controller = courseController

@router.post("/")
async def assign_subject_to_course(course: courseModel):
    return await course_controller.assign_subject_to_course(course)

@router.get("/")
async def fetch_course():
    return await course_controller.fetch_course()

@router.delete("/{id}")
async def delete_course(id: str):
    return await course_controller.delete_course(id)   
@router.put("/{id}")
async def update_course(id: str, course: courseModel):
    return await course_controller.edit_course(id, course)
@router.get("/{id}")
async def get_course(id: str):
    return await course_controller.course_detail(id)
 
