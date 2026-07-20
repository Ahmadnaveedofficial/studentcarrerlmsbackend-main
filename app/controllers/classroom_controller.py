from app.config.db import classroom_collection,collection2,student_collection,admin_collection
from app.models.classroomSchema import classroomModel
from app.models.studentSchema import studentModel, StudentList
from bson import ObjectId
class classroomController:
    @staticmethod
    async def create_classroom(classroom: classroomModel):
        try:
           
            if classroom.teacherId:
                
                teacher = collection2.find_one({"_id": ObjectId(classroom.teacherId)})
                if not teacher:
                    return {"error": "Teacher not found"}
            
            new_classroom = {
                "classroom_name": classroom.classroom_name,
                "students": classroom.students,  
                "teacherId": classroom.teacherId
            }
            
            print(new_classroom)

            result = classroom_collection.insert_one(new_classroom)

            return {
                "message": "Classroom successfully created",
                "id": str(result.inserted_id)
            }

        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def fetch_classrooms():
        try:
            classrooms = list(classroom_collection.find())

            for cls in classrooms:
                cls["_id"] = str(cls["_id"])

                # convert teacherId
                if cls.get("teacherId"):
                    cls["teacherId"] = str(cls["teacherId"])

                # convert students list
                if "students" in cls:
                    cls["students"] = [str(sid) for sid in cls["students"]]

            return {
                "message": "Classrooms fetched successfully",
                "data": classrooms
            }

        except Exception as e:
            return {"error": str(e)}

   
    
    @staticmethod
    async def delete_classroom(id: str):
        try:
            result = classroom_collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count > 0:
                return {"message": "Classroom deleted successfully"}
            else:
                return {"message": "Classroom not found"}
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def update_classroom(id: str, classroom: classroomModel):
        try:
            result = classroom_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": classroom.dict()}
            )
            if result.modified_count > 0:
                return {"message": "Classroom updated successfully"}
            else:
                return {"message": "Classroom not found"}
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def classroom_detail(id: str):
        try:
            classroom = classroom_collection.find_one({"_id": ObjectId(id)})
            if not classroom:
                return {"error": "Classroom not found"}

            classroom_id = str(classroom["_id"])

            # -------- TEACHER --------
            teacher_info = None
            teacher_id = classroom.get("teacherId")
            if teacher_id:
                teacher_doc = collection2.find_one({"_id": ObjectId(teacher_id)})
                if teacher_doc:
                    teacher_info = {
                        "_id": str(teacher_doc["_id"]),
                        "name": teacher_doc.get("name")
                    }

            # -------- STUDENTS --------
            student_ids = classroom.get("students", [])

            object_ids = []
            for sid in student_ids:
                try:
                    object_ids.append(ObjectId(sid))
                except Exception:
                    pass

            students = list(
                student_collection.find(
                    {"_id": {"$in": object_ids}},
                    {"name": 1}
                )
            )

            student_list = [
                {
                    "_id": str(student["_id"]),
                    "name": student.get("name")
                }
                for student in students
            ]

            return {
                "_id": classroom_id,
                "classroom_name": classroom.get("classroom_name"),
                "students": student_list,
                "teacher": teacher_info
            }

        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def add_student(classroom_id: str, data: StudentList):
        try:
            classroom = classroom_collection.find_one(
                {"_id": ObjectId(classroom_id)}
            )

            if not classroom:
                return {"message": "Classroom not found"}

            classroom_name = classroom.get("classroom_name")

            student_ids = data.student_ids   # keep them as strings

            # check students exist
            students_found = list(
                student_collection.find(
                    {"_id": {"$in": [ObjectId(sid) for sid in student_ids]}}
                )
            )

            if len(students_found) != len(student_ids):
                return {"message": "One or more student IDs are invalid"}

            # check duplicate student in same class name
            existing_classrooms = list(
                classroom_collection.find(
                    {
                        "classroom_name": classroom_name,
                        "students": {"$in": student_ids}
                    }
                )
            )

            if existing_classrooms:
                return {
                    "message": "One or more students already assigned to this class name"
                }

            # store as STRING
            classroom_collection.update_one(
                {"_id": ObjectId(classroom_id)},
                {"$addToSet": {"students": {"$each": student_ids}}}
            )

            return {"message": "Students added successfully"}

        except Exception as e:
            return {"error": str(e)}