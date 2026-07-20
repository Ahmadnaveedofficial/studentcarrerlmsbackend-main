from pydantic import BaseModel,fields
from typing import Optional
from bson import ObjectId


class TeacherModel(BaseModel):
    name: str
    email: str
    Teacher_Professionality: Optional[str] = None
    Teacher_Designation: Optional[str] = None
    Teacher_Phone_Number: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None
    password: Optional[str] = None  
class ChangePassword(BaseModel):
    email: str
    new_password: str
class subjectModel(BaseModel):
    subject_name: str
    subjectId: str
    description: Optional[str] = None
    
class courseModel(BaseModel):
    course_name: str
    course_code: Optional[str] = None
    description: Optional[str] = None
    teacherId: Optional[str] = None
    subjectId: str
    
   
    