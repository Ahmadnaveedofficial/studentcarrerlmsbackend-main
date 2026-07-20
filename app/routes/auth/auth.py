from fastapi import APIRouter
from app.controllers.auth_controller import AuthControllers
from app.controllers.Teacher_controller import TeacherController
from app.models.adminSchema import Admin, LoginSchema

router = APIRouter(
    tags=["Login Admin"]
)

auth_controller = AuthControllers()
teacher_controller = TeacherController()

@router.post("/register")
async def create_admin(admin: Admin):
    return await auth_controller.admin_panel(admin)

@router.post("/login")
async def admin_login(user: LoginSchema):
    return await auth_controller.admin_login(user)