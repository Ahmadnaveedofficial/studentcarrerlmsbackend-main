from fastapi import APIRouter
from app.controllers.TeacherGrading_controller import TeacherGradingController
from app.models.GradingSchema import GradingPayload

router = APIRouter(
    tags=["Teacher Grading"]
)
teacher_grading_controller = TeacherGradingController

@router.post("/teacher/grading/{assesmentId}")
async def assign_grading(grades: GradingPayload, assesmentId: str):
    return TeacherGradingController.assign_grading(grades, assesmentId)

@router.get("/teacher/grading/{assesmentId}")
async def get_grading_by_assesmentId(assesmentId: str):
    return TeacherGradingController.get_grading_by_assesmentId(assesmentId)

@router.get("/grading/{assesmentId}")
def get_studentid_by_assesmentId(assesmentId: str):
    return  TeacherGradingController.get_students_by_assessment(assesmentId)
@router.put("/grading/{assesmentId}/{studentId}")
def update_student_grades(assesmentId: str, studentId: str, marks: int):
    return TeacherGradingController.update_student_marks(assesmentId, studentId, marks)