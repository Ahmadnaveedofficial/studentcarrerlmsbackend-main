# from app.config.db import grading_collection,student_collection
# from bson import ObjectId

# class StudentShowGradesController:
  

#             @staticmethod
#             def showgrades_of_student_by_using_assesmentID(assesmnetId: str, studentId: str):
#                 try:
#                     grading = grading_collection.find_one({"assesmentId": assesmnetId})

#                     if not grading:
#                         return {"status": "error", "message": "Grading not found"}

#                     students = []
#                     for student in grading.get("students", []):

#                         student_obj_id = student["student_id"]

                     
#                         if isinstance(student_obj_id, str):
#                             student_obj_id = ObjectId(student_obj_id)

#                         student_data = student_collection.find_one(
#                             {"_id": student_obj_id}
#                         )

                        
#                         if student_data and student_data["student_id"] == studentId:
#                             students.append({
#                                 "student_id": student_data["student_id"],
#                                 "marks": student["marks"]
#                             })

#                     return {
#                         "status": "success",
#                         "weightage": grading["weightage"],
#                         "assesmentId": grading["assesmentId"],
#                         "students": students
#                     }

#                 except Exception as e:
#                     return {"status": "error", "message": str(e)}







from app.config.db import grading_collection,student_collection
from bson import ObjectId

class StudentShowGradesController:
  

            @staticmethod
            def showgrades_of_student_by_using_assesmentID(assesmnetId: str, studentId: str):
                try:
                    grading = grading_collection.find_one({"assesmentId": assesmnetId})

                    if not grading:
                        return {"status": "error", "message": "Grading not found"}

                    students = []
                    for student in grading.get("students", []):

                        student_obj_id = student["student_id"]

                     
                        if isinstance(student_obj_id, str):
                            student_obj_id = ObjectId(student_obj_id)

                        student_data = student_collection.find_one(
                            {"_id": student_obj_id}
                        )

                        
                        if student_data and student_data.get("student_user_id") == studentId:
                            students.append({
                                "student_id": student_data.get("student_user_id"),
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