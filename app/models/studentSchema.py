from pydantic import BaseModel
from typing import Optional, List


class studentModel(BaseModel):
    name: str
    email: str
    state: str
    Roll_Number: str
    city: str
    address: str
    date_of_birth: str 
    phone_number: str
    image_url: Optional[str] = None

class StudentList(BaseModel):
    student_ids: List[str]
    
    

class changePasswordModel(BaseModel):
    email: str
    new_password: str