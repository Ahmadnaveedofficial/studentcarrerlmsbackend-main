from app.config.db import course_collection, collection2, subject_collection
from app.models.TeacherSchema import courseModel
from bson import ObjectId

class CourseController:
    @staticmethod
    async def assign_subject_to_course(course: courseModel):
        try:
            new_course = {
                "course_name": course.course_name,
                "course_code": course.course_code,
                "description": course.description,
                "subjectId": course.subjectId,
                "teacherId": course.teacherId,
            }
            registered_course = course_collection.insert_one(new_course)
            return {
                "message": "Course successfully assigned to Teacher and Subject",
                "id": str(registered_course.inserted_id),
            }
        except Exception as e:
            return {"error": str(e)}



    @staticmethod
    async def fetch_course():
        try:
            courses = list(course_collection.find())
            normalized_courses = []

            for course in courses:
               
                teacher = None
                if course.get("teacherId"):
                    try:
                        teacher = collection2.find_one({"_id": ObjectId(course["teacherId"])})
                    except Exception:
                        teacher = None 

                
                subject = None
                if course.get("subjectId"):
                    try:
                        subject = subject_collection.find_one({"_id": ObjectId(course["subjectId"])})
                    except Exception:
                        subject = None 

                normalized_course = {
                    "_id": str(course["_id"]),
                    "name": course.get("course_name"),
                    "course_code": course.get("course_code"),
                    "description": course.get("description"),

                    "teacher": {
                        "_id": str(teacher["_id"]),
                        "name": teacher.get("name")
                    } if teacher else None,

                    "subject": {
                        "_id": str(subject["_id"]),
                        "name": subject.get("subject_name")
                    } if subject else None
                }

                normalized_courses.append(normalized_course)

            return {"courses": normalized_courses}

        except Exception as e:
            return {"error": str(e)}

    
    @staticmethod
    async def delete_course(id:str):
        try:
            result= course_collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count == 1:
                return {"message": "Course successfully deleted"}
            else:
                return {"message": "Course not found"}
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def edit_course(id:str, course: courseModel):
        try:
            course_update= course_collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": course.dict()}
            )
            if course_update.modified_count == 1:
                return {"message": "Course successfully updated"}
            else:
                return {"message": "Course not found or no changes made"}
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def course_detail(id: str):
        try:
            course = course_collection.find_one({"_id": ObjectId(id)})
            course["_id"] = str(course["_id"])
            return course
        except Exception as e:
            return {"error": str(e)}
        
courseController = CourseController()
