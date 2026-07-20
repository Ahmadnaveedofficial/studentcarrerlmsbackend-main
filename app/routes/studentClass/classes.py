from fastapi import APIRouter
from app.controllers.studentClassController import StudentClassController
router = APIRouter(
    tags=["Name Get By ID/ Student Classes Get By user id"]
)
student_class_controller = StudentClassController()

@router.get("/classes/student/{student_id}")
async def get_student_classes(student_id: str):
    return await student_class_controller.get_students_by_classroom(student_id)

@router.get("/classes/teacher/{teacher_id}")
async def get_teacher_name(teacher_id: str):
    return await student_class_controller.get_teacher_name(teacher_id)

@router.get("/classes/teacher/user/{teacher_user_id}")
async def get_teacher_name_by_user_id(teacher_user_id: str):
    return await student_class_controller.get_teacher_name_by_userId(teacher_user_id)

@router.get("/classes/classroom/{classroom_id}")
async def get_classroom_name(classroom_id: str):
    return await student_class_controller.get_classroom_name(classroom_id)

@router.get("/classes/timetable/{user_id}")
async def get_time_table_by_user(user_id: str):
    return await student_class_controller.get_time_table_by_student(user_id)

@router.get("/classes/student/user/{student_user_id}")
async def get_student_name_by_user_id(student_user_id: str):
    return await student_class_controller.get_name_of_student_by_user_id(student_user_id)

@router.get("/classes/teacher/email/{teacher_user_id}")
async def get_teacher_email_by_user_id(teacher_user_id: str):
    return await student_class_controller.get_teacher_email_by_user_id(teacher_user_id)

@router.get("/classes/student/email/{student_user_id}")
async def get_student_email_by_user_id(student_user_id: str):
    return await student_class_controller.get_student_email_by_user_id(student_user_id)

@router.get("/classes/student/id/{student_id}")
async def get_student_name_by_id(student_id: str):
    return await student_class_controller.get_student_name_by_id(student_id)

@router.get("/classes/student/user/id/{student_user_id}")
async def get_student_id_by_user_id(student_user_id: str):
    return await student_class_controller.get_student_ID_by_user_id(student_user_id)