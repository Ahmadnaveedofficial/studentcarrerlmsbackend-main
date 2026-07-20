from fastapi import APIRouter, UploadFile, File, Form
from app.controllers.studentUploadAssesment_controller import StudentUploadAssesmentController
from app.models.AssesmentSchema import AssesmentResponseModel
from app.config.db import Upload_assessment_collection

router = APIRouter(tags=["Student Upload Assesment"])

@router.post("/upload-assessment/{AssesmentId}")
async def upload_assessment(
    AssesmentId: str,
    teacherId: str = Form(...),
    classroomId: str = Form(...),
    studentId: str = Form(...),
    image: UploadFile = File(...)
):
    model = AssesmentResponseModel(
        teacherId=teacherId,
        classroomId=classroomId,
        studentId=studentId,
        upload_assesment=""
    )

    return await StudentUploadAssesmentController.upload_assesent(
        model, image, AssesmentId
    )


@router.get("/student/submission/{assessmentId}/{studentId}")
async def get_student_submission(assessmentId: str, studentId: str):
    return await StudentUploadAssesmentController.get_student_submission(assessmentId, studentId)
    
@router.get("/teacher/submission/{assessmentId}/{teacherId}")
async def get_teacher_submission(assessmentId: str, teacherId: str):
    return await StudentUploadAssesmentController.get_student_submissions(assessmentId, teacherId)