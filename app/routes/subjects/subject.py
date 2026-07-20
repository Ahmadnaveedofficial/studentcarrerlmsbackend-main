from fastapi import APIRouter
from app.controllers.subject_controllers import subjectController
from app.models.TeacherSchema import subjectModel

router = APIRouter(
    prefix="/teacher/subject",
    tags=["Teacher Subjects"]
)

# Controller instance (no need to recreate)
subject_controller = subjectController

@router.get("/")
async def fetch_subjects():
    return await subject_controller.fetch_subjects()

@router.delete("/{id}")
async def delete_subject(id: str):
    return await subject_controller.delete_subject(id)

@router.post("/")
async def subjectsof_Teacher(subject: subjectModel):
    return await subject_controller.subjectsof_Teacher(subject)
@router.put("/{id}")
async def update_subject(id: str, subject: subjectModel):
    return await subject_controller.update_subject(id, subject)
@router.get("/{id}")
async def subject_detail(id: str):
    return await subject_controller.subject_detail(id)