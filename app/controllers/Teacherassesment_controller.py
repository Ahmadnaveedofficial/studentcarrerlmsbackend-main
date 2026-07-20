from app.config.db import assesment_collection, classroom_collection,collection2,grading_collection
from app.models.AssesmentSchema import AssesmentModel
from bson import ObjectId
from datetime import datetime


class TeacherAssesmentController:

    @staticmethod
    def create_assesment(assesment: AssesmentModel):

        classroom = classroom_collection.find_one({"_id": ObjectId(assesment.classId)})
        if not classroom:
            return {"status": "error", "message": "Classroom not found"}
        

        

        assesment_data = {
            "name": assesment.name,
            "description": assesment.description,
            "classId": classroom["_id"],
            "teacherId": assesment.teacherId,
            "created_at": datetime.utcnow()
        }

        result = assesment_collection.insert_one(assesment_data)

        return {
            "message": "Assignment created successfully",
            "assesment_id": str(result.inserted_id)
        }


  
    @staticmethod
    def get_assesments_by_teacher(class_id: str):
        try:
            class_object_id = ObjectId(class_id)

            classroom = classroom_collection.find_one({"_id": class_object_id})
            if not classroom:
                return {"status": "error", "message": "Classroom not found"}

            assesments = list(
                assesment_collection.find({"classId": class_object_id})
            )

            for assesment in assesments:
                assesment["_id"] = str(assesment["_id"])
                assesment["classId"] = str(assesment["classId"]) 

            return {"status": "success", "data": assesments}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    async def delete_assesment(assesment_id: str):
        try:
            obj_id = ObjectId(assesment_id)

            # Delete grades (use string field + correct key name)
            grades_result = grading_collection.delete_many({
                "assesmentId": assesment_id
            })

            # Delete assessment
            result = assesment_collection.delete_one({
                "_id": obj_id
            })

            if result.deleted_count == 0:
                return {"status": "error", "message": "Assesment not found"}

            return {
                "status": "success",
                "message": "Assesment deleted successfully",
                "deleted_grades": grades_result.deleted_count
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}
    @staticmethod
    async def all_assesments_get(teacher_id: str):
        try:
            teacher_object_id = str(teacher_id)
            assesments = list(
                assesment_collection.find({"teacherId": teacher_object_id})
            )
            for assesment in assesments:
                assesment["_id"] = str(assesment["_id"])
                assesment["classId"] = str(assesment["classId"])
                assesment["teacherId"] = str(assesment["teacherId"])
            return {"status": "success", "data": assesments}
        except Exception as e:
            return {"status": "error", "message": str(e)}
