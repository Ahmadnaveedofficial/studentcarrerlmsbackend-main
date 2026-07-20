from app.config.db import classroom_collection, collection2
from bson import ObjectId


class TeacherClassController:

    @staticmethod
    def show_classes_to_assign_teacher(teacher_user_id: str):
        try:
            if not teacher_user_id:
                return {"status": "error", "message": "Teacher user ID is required"}

            teacher = collection2.find_one({"teacher_user_id": teacher_user_id})
            if not teacher:
                return {"status": "error", "message": "Teacher not found"}
            print(teacher)

            teacher_id = str(teacher["_id"])
            print(teacher_id)

            classes = list(classroom_collection.find({"teacherId": teacher_id}))
            print(classes)

            for classroom in classes:
                classroom["_id"] = str(classroom["_id"])
                classroom["teacherId"] = str(classroom["teacherId"])

            return {"status": "success", "data": classes}

        except Exception as e:
            return {"status": "error", "message": str(e)}
