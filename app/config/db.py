from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

mongo_uri= os.getenv("MONGOAPI")

if not mongo_uri:
    print("Cannot access the mongo URL in the .env file :")

try:
    client= MongoClient(mongo_uri)
    db= client["StudentCarrerlms"]
    admin_collection= db["users"]
    collection2= db["Teacher"]
    subject_collection= db["Subjects"]
    course_collection= db["Courses"]
    student_collection= db["Student"]
    classroom_collection= db["Classroom"]
    attendence_collection= db["Attendance"]
    assesment_collection= db["Assesment"]
    Teacher_time_table_collection= db["Teacher_time_table"]
    student_time_table_collection= db["Student_time_table"]
    Upload_assessment_collection= db["Upload_assessment"]
    notifications= db["Notifications"]
    grading_collection= db["Grading"]

    print("connection was successfully initialized ")

except Exception as e:
    print("MongoDB connection failed:", e)