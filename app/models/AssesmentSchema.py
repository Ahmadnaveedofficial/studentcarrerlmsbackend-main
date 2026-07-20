from pydantic import BaseModel
from bson import ObjectId

class AssesmentModel(BaseModel):
    name: str
    description: str
    classId: str
    teacherId: str

class AssesmentResponseModel(BaseModel):
    upload_assesment: str
    teacherId: str
    classroomId: str
    studentId: str
