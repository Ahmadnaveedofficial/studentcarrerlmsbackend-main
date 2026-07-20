from pydantic import BaseModel
from typing import List

class AttendanceItem(BaseModel):
    student_id: str
    status: str 

class AttendancePayload(BaseModel):
    classroom_id: str
    attendance: List[AttendanceItem]
