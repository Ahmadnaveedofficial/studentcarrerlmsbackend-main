from pydantic import BaseModel
from typing import List, Optional
from datetime import time

class TimeSlot(BaseModel):
    day: str
    start_time: time
    end_time: time
    teacher_id: str
    classroom_id: str
    date: Optional[str] = None
    roomno: Optional[str] = None