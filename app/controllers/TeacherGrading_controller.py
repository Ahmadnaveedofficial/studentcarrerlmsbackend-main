from bson import ObjectId
from datetime import datetime
from app.config.db import grading_collection,assesment_collection,classroom_collection
from app.models.GradingSchema import GradingPayload

class TeacherGradingController:

   

    @staticmethod
    def assign_grading(data: GradingPayload, assesmnetId: str):
        try:
            
            existing = grading_collection.find_one({
                "assesmentId": assesmnetId
            })

           
            new_students = [
                {
                    "student_id": item.student_id,
                    "marks": item.marks
                }
                for item in data.grades
            ]

            
            if not existing:
                grading_collection.insert_one({
                    "assesmentId": data.assesmentId,
                    "teacherId": data.teacherId,
                    "weightage": data.weightage,
                    "students": new_students,
                })

                return {
                    "status": "success",
                    "message": "Grading assigned successfully (new record)"
                }

            
            existing_student_ids = {
                student["student_id"]
                for student in existing.get("students", [])
            }

            students_to_add = [
                student for student in new_students
                if student["student_id"] not in existing_student_ids
            ]

            # 4️⃣ Only push new students (no override)
            if students_to_add:
                grading_collection.update_one(
                    {"assesmentId": data.assesmentId},
                    {
                        "$push": {
                            "students": {
                                "$each": students_to_add
                            }
                        }
                    }
                )

                return {
                    "status": "success",
                    "message": "New students added, existing not modified"
                }

            return {
                "status": "success",
                "message": "No new students to add"
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}


    @staticmethod
    def get_grading_by_assesmentId(assesmentId: str):
        try:
            grading = grading_collection.find_one({"assesmentId": assesmentId})

            if not grading:
                return {"status": "error", "message": "Grading not found"}

           
            students = []
            for student in grading.get("students", []):
                students.append({
                    "student_id": str(student["student_id"]),
                    "marks": student["marks"]
                })

            return {
                "status": "success",
                "weightage": grading["weightage"],
                "assesmentId": grading["assesmentId"],
                "students": students
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}
        
    @staticmethod
    def get_students_by_assessment(assesment_id: str):
        try:
            obj_id = ObjectId(assesment_id)
            assessment = assesment_collection.find_one({"_id": obj_id})
            if not assessment:
                return {"status": "error", "message": "Assessment not found"}
            class_id = assessment.get("classId")
            class_doc = classroom_collection.find_one({"_id": ObjectId(class_id)})
            if not class_doc:
                return {"status": "error", "message": "Class not found"}
            students = class_doc.get("students", [])
            return {
                "status": "success",
                "students": students,
                "total_students": len(students)
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    @staticmethod
    def update_student_marks(assesmentId: str, studentId: str, marks: int):
        try:
            result = grading_collection.update_one(
                {
                    "assesmentId": assesmentId,
                    "students.student_id": studentId
                },
                {
                    "$set": {
                        "students.$.marks": marks
                    }
                }
            )

            if result.matched_count == 0:
                return {"status": "error", "message": "Student or grading not found"}

            return {"status": "success", "message": "Student marks updated successfully"}

        except Exception as e:
            return {"status": "error", "message": str(e)}