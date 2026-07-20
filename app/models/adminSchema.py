import enum
from pydantic import BaseModel, EmailStr



class Admin(BaseModel):
    email: EmailStr= "haidernawab067@gmail.com"
    password: str = "amazf123"
    role : str  = "ADMIN"


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

