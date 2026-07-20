# from bson import ObjectId
# from app.config.db import attendence_collection, student_collection


# class StudentAttendenceController:

#     @staticmethod
#     async def get_student_attendance(user_id: str, classroom_id: str):

#         try:
#             classroom_object_id = ObjectId(classroom_id)
#         except:
#             return {"error": "Invalid classroom ID format"}

#         student = student_collection.find_one({
#             "student_id": user_id
#         })

#         if not student:
#             return {"error": "Student not found"}

#         student_object_id = student["_id"]

#         attendences = list(
#             attendence_collection.find(
#                 {
#                     "classroom_id": classroom_object_id,
#                     "students.student_id": student_object_id
#                 }
#             )
#         )

#         result = []

#         for attendence in attendences:

#             for student_record in attendence.get("students", []):

#                 if student_record.get("student_id") == student_object_id:

#                     result.append({
#                         "attendance_id": str(attendence["_id"]),
#                         "student_id": str(student_object_id),
#                         "user_id": user_id,
#                         "student_name": student.get("name"),
#                         "roll_number": student.get("Roll_Number"),
#                         "classroom_id": classroom_id,
#                         "date": attendence.get("date"),
#                         "status": student_record.get("status")
#                     })

#         return result







from bson import ObjectId
from app.config.db import attendence_collection, student_collection


class StudentAttendenceController:

    @staticmethod
    async def get_student_attendance(user_id: str, classroom_id: str):

        try:
            classroom_object_id = ObjectId(classroom_id)
        except:
            return {"error": "Invalid classroom ID format"}

        student = student_collection.find_one({
            "student_user_id": user_id
        })

        if not student:
            return {"error": "Student not found"}

        student_object_id = student["_id"]

        attendences = list(
            attendence_collection.find(
                {
                    "classroom_id": classroom_object_id,
                    "students.student_id": student_object_id
                }
            )
        )

        result = []

        for attendence in attendences:

            for student_record in attendence.get("students", []):

                if student_record.get("student_id") == student_object_id:

                    result.append({
                        "attendance_id": str(attendence["_id"]),
                        "student_id": str(student_object_id),
                        "user_id": user_id,
                        "student_name": student.get("name"),
                        "roll_number": student.get("Roll_Number"),
                        "classroom_id": classroom_id,
                        "date": attendence.get("date"),
                        "status": student_record.get("status")
                    })

        return result