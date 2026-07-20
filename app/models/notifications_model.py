from pydantic import BaseModel
from typing import Optional

class Notification(BaseModel):
    teacher_id: str
    message: str
    is_read: Optional[bool] = False