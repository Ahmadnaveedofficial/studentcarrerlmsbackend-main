from pydantic import BaseModel
from typing import List

class StudentMarks(BaseModel):
    student_id: str
    marks: int

class GradingPayload(BaseModel):
    assesmentId: str
    teacherId: str
    weightage: int
    grades: List[StudentMarks]