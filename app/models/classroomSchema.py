from typing import List, Optional
from pydantic import BaseModel, Field

class classroomModel(BaseModel):
    classroom_name: str
    students: List[str] = Field(default_factory=list)  # <-- correct
    teacherId: Optional[str] = None

class StudentList(BaseModel):
    student_ids: List[str] = Field(default_factory=list)  # <-- correct