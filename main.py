from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import auth
from app.routes.Teacher import Teacher
from app.routes.subjects.subject import router as subject_router
from app.routes.course.course import router as course_router
from app.routes.student import student
from app.routes.classroom import classroom
from app.routes.TeacherClass import classAssign
from app.routes.Attendence import attendance
from app.routes.Assesment import assign
from app.routes.studentClass import classes
from app.routes.TeacherTimeTable import timetable
from app.routes.StudentAttendence import attendence
from app.routes.studentAssesment import Assesment
from app.routes.StudentUploadAssesmnet import upload
from app.routes.TeacherGrading import grading
from app.routes.studentGrades import showgrades
from app.routes.notifications import notifications_route



app = FastAPI(title="Login System API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(Teacher.router)
app.include_router(student.router)
app.include_router(classroom.router)
app.include_router(attendance.router)
app.include_router(classAssign.router)
app.include_router(assign.router)
app.include_router(classes.router)
app.include_router(timetable.router)
app.include_router(attendence.router)
app.include_router(Assesment.router)
app.include_router(upload.router)
app.include_router(grading.router)
app.include_router(showgrades.router)
app.include_router(notifications_route.router)



app.include_router(subject_router)
app.include_router(course_router)



@app.get("/")
def root():
    return {"message": "Welcome to the Student Management System API!"}
