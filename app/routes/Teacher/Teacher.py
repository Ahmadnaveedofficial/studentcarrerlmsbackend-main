from fastapi import APIRouter, Form, File, UploadFile
from app.controllers.Teacher_controller import TeacherController
from app.models.TeacherSchema import TeacherModel, ChangePassword
from app.models.adminSchema import Admin

router = APIRouter(
    tags=["Teacher"]
)
teacher_controller = TeacherController()




# ✅ Create teacher
@router.post("/teacher_Added")
async def create_teacher(
    name: str = Form(...),
    email: str = Form(...),
    Teacher_Professionality: str = Form(...),
    Teacher_Designation: str = Form(...),
    Teacher_Phone_Number: str = Form(...),
    image: UploadFile = File(...),
):
    teacher_data = TeacherModel(
        name=name,
        email=email,
        Teacher_Professionality=Teacher_Professionality,
        Teacher_Designation=Teacher_Designation,
        Teacher_Phone_Number=Teacher_Phone_Number,
    )
    return await TeacherController.create_teacher(teacher_data, image)

# ✅ Delete teacher
@router.delete("/teacher/{id}")
async def delete_teacher(id: str):
    return await teacher_controller.delete_teacher(id)

# ✅ Update teacher
@router.put("/teacher/{id}")
async def update_teacher(id: str, teacher: TeacherModel):
    return await teacher_controller.update_Teacher(id, teacher)
@router.get("/teacher/{id}")
async def Teacher_detail(id: str):
    return await teacher_controller.Teacher_detail(id)
# ✅ Get all teachers
@router.get("/teacher")
async def all_teacher_fetch():
    return await teacher_controller.all_teacher_fetch()

@router.put("/teacher/password/change")
async def change_teacher_password(password_data: ChangePassword):
    return await teacher_controller.change_teacher_password(password_data)

@router.get("/teacher/user/{teacher_user_id}")
async def get_teacher_detail_by_userId(teacher_user_id:str):
    return await teacher_controller.get_teacher_detail_by_userId(teacher_user_id)