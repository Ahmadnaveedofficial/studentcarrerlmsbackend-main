from fastapi import APIRouter, Form, File, UploadFile
from app.controllers.student_controller import StudentController
from app.models.studentSchema import studentModel, changePasswordModel

router = APIRouter(
    tags=["Student"]
)
student_controller = StudentController()

@router.post("/student_Added")
async def student_added(
    name: str = Form(...),
    email: str = Form(...),
    state: str = Form(...),
    Roll_Number: str = Form(...),
    city: str = Form(...),
    address: str = Form(...),
    date_of_birth: str = Form(...),
    phone_number: str = Form(...),
    image_url: UploadFile | None = File(None),
):

    class Student: pass

    student = Student()
    student.name = name
    student.email = email
    student.state = state
    student.Roll_Number = Roll_Number
    student.city = city
    student.address = address
    student.date_of_birth = date_of_birth
    student.phone_number = phone_number

    return await StudentController.create_student(student, image_url)

@router.get("/Student")
async def all_student_fetch():
    return await student_controller.all_student_fetch()

@router.get("/student/{id}")
async def student_detail(id: str):
    return await student_controller.student_detail(id)

@router.put("/student/{id}")
async def update_student(
    id: str,
    name: str = Form(...),
    email: str = Form(...),
    state: str = Form(...),
    roll_number: str = Form(...),
    city: str = Form(...),
    address: str = Form(...),
    date_of_birth: str = Form(...),
    phone_number: str = Form(...),
    image_url: UploadFile = File(None),  
):
    student_data = studentModel(
        name=name,
        email=email,
        state=state,
        city=city,
        Roll_Number=roll_number,
        address=address,
        date_of_birth=date_of_birth,
        phone_number=phone_number,
    )


    return await student_controller.update_student_data(id, student_data, image_url)

@router.delete("/student/{id}")
async def delete_student(id: str):
    return await student_controller.delete_student(id)


@router.put("/change_student_password")
async def change_student_password(change_password: changePasswordModel):
    return await student_controller.change_student_password(change_password)