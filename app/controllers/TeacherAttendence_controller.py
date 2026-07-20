from bson import ObjectId
from datetime import datetime, timedelta
from app.config.db import classroom_collection, attendence_collection
from app.models.AttendenceSchema import AttendancePayload

class TeacherAttendenceController:

    @staticmethod
    def normalize_status(status: str) -> str:
        status = status.lower()
        if status in ("p", "present"):
            return "present"
        if status in ("a", "absent"):
            return "absent"
        raise ValueError("Invalid attendance status")

    @staticmethod
    async def mark_attendance(data: AttendancePayload):
        try:
            classroom_id = ObjectId(data.classroom_id)

            # 1️⃣ Validate classroom
            classroom = classroom_collection.find_one({"_id": classroom_id})
            if not classroom:
                return {"status": "error", "message": "Classroom not found"}

            # 2️⃣ Classroom students (list of IDs)
            classroom_student_ids = {
                str(student_id) for student_id in classroom.get("students", [])
            }

            # 3️⃣ Normalize today's date (UTC)
            today_start = datetime.utcnow().replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            today_end = today_start + timedelta(days=1)

            # 4️⃣ Student ObjectIds from payload
            payload_student_ids = [
                ObjectId(item.student_id) for item in data.attendance
            ]

            # 5️⃣ Check duplicate attendance
            already_marked = attendence_collection.find_one({
                "classroom_id": classroom_id,
                "date": {"$gte": today_start, "$lt": today_end},
                "students.student_id": {"$in": payload_student_ids}
            })

            if already_marked:
                return {
                    "status": "error",
                    "message": "Attendance already marked for today"
                }

            # 6️⃣ Build attendance array
            students_attendance = []

            for item in data.attendance:
                if item.student_id not in classroom_student_ids:
                    return {
                        "status": "error",
                        "message": f"Student {item.student_id} not in classroom"
                    }

                students_attendance.append({
                    "student_id": ObjectId(item.student_id),
                    "status": TeacherAttendenceController.normalize_status(item.status)
                })

            # 7️⃣ Insert attendance document
            attendence_collection.insert_one({
                "classroom_id": classroom_id,
                "date": datetime.utcnow(),
                "students": students_attendance
            })

            return {
                "status": "success",
                "message": "Attendance recorded successfully"
            }

        except ValueError as ve:
            return {"status": "error", "message": str(ve)}
        except Exception as e:
            return {"status": "error", "message": "Internal server error"}