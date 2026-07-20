from app.config.db import Upload_assessment_collection,assesment_collection,student_collection,grading_collection
from app.models.AssesmentSchema import AssesmentResponseModel
from bson import ObjectId
from app.config.config import supabase
import os
import uuid
from app.controllers.notifications_controller import NotificationController
from app.models.notifications_model import Notification


class StudentUploadAssesmentController:
    @staticmethod
    async def upload_assesent(AssesmentResponseModel: AssesmentResponseModel, image, AssesmentId:str):
        try:
            assement= assesment_collection.find_one({"_id": ObjectId(AssesmentId)})
            if not assement:
                return {"error": "Assesment not found"}
            image_url= None
            if image:
                image_data = await image.read()
                image_name = f"{uuid.uuid4()}_{image.filename}"
                bucket_name = os.getenv("SUPABASE_BUCKET", "Student_Assesmnet")

                file_path = f"public/{image_name}"

                res = supabase.storage.from_(bucket_name).upload(
                    file_path,
                    image_data,
                    file_options={
                        "content-type": image.content_type or "application/octet-stream"
                    }
                )

                if not res:
                    raise Exception("Failed to upload image to Supabase")

                image_url = supabase.storage.from_(bucket_name).get_public_url(file_path)
                
            upload_assessment = {
                    "assessmentId": AssesmentId,
                    "teacherId": AssesmentResponseModel.teacherId,
                    "classroomId": AssesmentResponseModel.classroomId,
                    "studentId": AssesmentResponseModel.studentId,
                    "upload_assesment": image_url
                }
            Upload_assessment_collection.insert_one(upload_assessment)

            student = student_collection.find_one({
                    "_id": ObjectId(AssesmentResponseModel.studentId)
                })

            notification = Notification(
                    teacher_id=AssesmentResponseModel.teacherId,
                    message=f"{student['name']} submitted an assessment"
                )

            await NotificationController.create_notification(notification)

            return {"message": "Assesment uploaded successfully"}
                    
        except Exception as e:
            return {"error": str(e)}
    
   
    @staticmethod
    async def get_student_submissions(assesmentId: str, teacherId: str):
        try:
            submissions = Upload_assessment_collection.find({
                "assessmentId": assesmentId,
                "teacherId": teacherId
            })

            submission_list = []

            for sub in submissions:
                sub["_id"] = str(sub["_id"])
                submission_list.append({
                    "studentId": sub["studentId"],
                    "file": sub["upload_assesment"]
                })

            if len(submission_list) == 0:
                return {"submitted": False, "data": []}

            return {
                "submitted": True,
                "data": submission_list
            }

        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def get_student_submission(assesmentId: str, studentId: str):
        try:
            # Step 1: Get student using student_user_id
            student = student_collection.find_one({"student_user_id": studentId})
            if not student:
                return {"status": "error", "message": "Student not found"}

            student_obj_id = student["_id"]

        # Step 2: Match based on how it's stored in upload collection
            submissions = Upload_assessment_collection.find({
                "assessmentId": assesmentId,
                "studentId": str(student_obj_id)   
            })

            submission_list = []

            for sub in submissions:
                submission_list.append({
                    "_id": str(sub["_id"]),
                    "studentId": sub["studentId"],
                    "file": sub.get("upload_assesment")
                })

            if not submission_list:
                return {"submitted": False, "data": []}

            return {
                "submitted": True,
                "data": submission_list
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}