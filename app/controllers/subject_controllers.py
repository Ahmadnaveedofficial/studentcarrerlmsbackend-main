from app.config.db import subject_collection
from bson import ObjectId
from app.models.TeacherSchema import subjectModel

class SubjectController:
    @staticmethod
    async def subjectsof_Teacher(subject: subjectModel):
        """Add a new subject"""
        try:
            new_subject = {
                "subject_name": subject.subject_name,
                "subjectId": subject.subjectId,
                "description": subject.description,
            }
            registered_subject = subject_collection.insert_one(new_subject)
            return {
                "message": "Subject successfully added to the Teacher",
                "id": str(registered_subject.inserted_id),
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def fetch_subjects():
        try:
            subjects = list(subject_collection.find())
            for subject in subjects:
                subject["_id"] = str(subject["_id"])
            return subjects
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def subject_detail(id: str):
        try:
            subject= subject_collection.find_one({"_id": ObjectId(id)})
            subject["_id"] = str(subject["_id"])
            return subject
        except Exception as e:
            return {"error": str(e)}
        
    @staticmethod
    async def update_subject(id: str, subject: subjectModel):
        try:
            result = subject_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": subject.dict()}
            )
            if result.modified_count > 0:
                return {"message": "Subject updated successfully"}
            else:
                return {"message": "Subject not found"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def delete_subject(id: str):
        try:
            result = subject_collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count > 0:
                return {"message": "Subject deleted successfully"}
            else:
                return {"message": "Subject not found"}
        except Exception as e:
            return {"error": str(e)}

# ✅ Create an instance for import
subjectController = SubjectController()
