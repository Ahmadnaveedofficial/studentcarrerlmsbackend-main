from fastapi import APIRouter
from app.controllers.studentShowgrades_controller import StudentShowGradesController

router = APIRouter(
    tags=["Student Grades"]
)
student_grades_controller = StudentShowGradesController


@router.get("/student/grades/{assesmnetId}/{studentId}")
def  viewgrades(assesmnetId: str, studentId: str):
    return student_grades_controller.showgrades_of_student_by_using_assesmentID(assesmnetId, studentId)

