# import traceback
# from app.config.db import classroom_collection, student_collection,collection2,Teacher_time_table_collection
# from bson import ObjectId


# def serialize_mongo(data):
#     if isinstance(data, list):
#         return [serialize_mongo(item) for item in data]

#     if isinstance(data, dict):
#         for key, value in data.items():
#             if isinstance(value, ObjectId):
#                 data[key] = str(value)
#             elif isinstance(value, (dict, list)):
#                 data[key] = serialize_mongo(value)

#     return data

# class StudentClassController:
#     @staticmethod
#     async def get_students_by_classroom(student_user_id: str):
#         try:
#             student = student_collection.find_one({"student_id": student_user_id})
#             if not student:
#                 return {"error": "Student not found"}

#             student["_id"] = str(student["_id"])

#             classrooms_cursor = classroom_collection.find(
#                 {"students": str(student["_id"])},
#                 {
#                     "_id": 1,
#                     "classroom_name": 1,
#                     "teacherId": 1
#                 }
#             )

#             classrooms = list(classrooms_cursor)

#             if not classrooms:
#                 return {"message": "No classes found"}

           
#             for classroom in classrooms:
#                 classroom["_id"] = str(classroom["_id"])
#                 classroom["teacherId"] = str(classroom["teacherId"])

#             return classrooms

#         except Exception as e:
#             return {"error": str(e)}

        
#     @staticmethod
#     async def get_teacher_name(teacher_id: str):
#         try:
#             teacher = collection2.find_one({"_id": ObjectId(teacher_id)})

#             if not teacher:
#                 return {"error": "Teacher not found"}

#             return {
#                 "_id": str(teacher["_id"]),
#                 "name": teacher.get("name", "No name found")
#             }

#         except Exception as e:
#             return {"error": str(e)}
#     @staticmethod
#     async def get_teacher_name_by_userId(teacher_user_id:str):
#         try:
#             teaher= collection2.find_one({"teacher_user_id": teacher_user_id})
#             if not teaher:
#                 return {"error": "Teacher not found"}
#             return {
#                 "_id": str(teaher["_id"]),
#                 "name": teaher.get("name", "No name found")
#             }       
#         except Exception as e:
#             return {
#                 "error": str(e)
#             }
    
#     @staticmethod
#     async def get_classroom_name(classroom_id: str):
#         try:
#             classroom = classroom_collection.find_one({"_id": ObjectId(classroom_id)})

#             if not classroom:
#                 return {"error": "Classroom not found"}

#             return {
#                 "_id": str(classroom["_id"]),
#                 "classroom_name": classroom.get("classroom_name", "No classroom name found")
#             }

#         except Exception as e:
#             return {"error": str(e)}
        
#     @staticmethod
#     async def get_time_table_by_student(student_id: str):
#         try:
#             student = student_collection.find_one({"student_id": student_id})
#             if not student:
#                 return {"error": "Student not found"}

#             student_id_str = str(student["_id"])

#             classrooms = list(
#                 classroom_collection.find(
#                     {"students": student_id_str},
#                     {"_id": 1, "classroom_name": 1, "teacherId": 1}
#                 )
#             )

#             if not classrooms:
#                 return {"message": "No classes found"}

#             time_tables = []

#             for classroom in classrooms:
#                 classroom_id_str = str(classroom["_id"])

#                 time_table = Teacher_time_table_collection.find_one(
#                     {"classroom_id": classroom_id_str}
#                 )

#                 if time_table:
#                     time_tables.append(time_table)

          
#             return serialize_mongo(time_tables)

#         except Exception as e:
#             traceback.print_exc()
#             return {"error": str(e)}
    
#     @staticmethod
#     async def get_name_of_student_by_user_id(student_user_id: str):
#         try:
#             student = student_collection.find_one({"student_id": student_user_id})
#             if not student:
#                 return {"error": "Student not found"}
#             return {
#                 "_id": str(student["_id"]),
#                 "name": student.get("name", "No name found")
#             }
#         except Exception as e:
#             return {"error": str(e)}
    
#     @staticmethod
#     async def get_student_email_by_user_id(student_user_id: str):
#         try:
#             student = student_collection.find_one({"student_id": student_user_id})
#             if not student:
#                 return {"error": "Student not found"}
#             return {
#                 "_id": str(student["_id"]), 
#                 "email": student.get("email", "No email found")
#             }
#         except Exception as e:
#             return {"error": str(e)}
        
    
#     @staticmethod
#     async def get_teacher_email_by_user_id(teacher_user_id: str):
#         try:
#             teacher = collection2.find_one({"teacher_user_id": teacher_user_id})
#             if not teacher:
#                 return {"error": "Teacher not found"}
#             return {
#                 "_id": str(teacher["_id"]), 
#                 "email": teacher.get("email", "No email found")
#             }
#         except Exception as e:
#             return {"error": str(e)}
    
#     @staticmethod
#     async def get_student_name_by_id(student_id: str):
#         try:
#             student = student_collection.find_one({"_id": ObjectId(student_id)})
#             if not student:
#                 return {"error": "Student not found"}
#             return {
#                 "_id": str(student["_id"]),
#                 "name": student.get("name", "No name found")
#             }
#         except Exception as e:
#             return {"error": str(e)}
#     @staticmethod
#     async def get_student_ID_by_user_id(student_user_id: str):
#             try:
#                 # Lookup student by your custom student_id field
#                 student = student_collection.find_one({"student_id": student_user_id})
#                 if not student:
#                     return {"status": "error", "message": "Student not found"}

#                 # Return MongoDB ObjectId (_id) as string
#                 return {
#                     "status": "success",
#                     "_id": str(student["_id"]),  # Convert ObjectId to string for JSON
#                     "student_id": student.get("student_id", "No student ID found")
#                 }

#             except Exception as e:
#                 return {"status": "error", "message": str(e)}








import traceback
from app.config.db import classroom_collection, student_collection,collection2,Teacher_time_table_collection
from bson import ObjectId


def serialize_mongo(data):
    if isinstance(data, list):
        return [serialize_mongo(item) for item in data]

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
            elif isinstance(value, (dict, list)):
                data[key] = serialize_mongo(value)

    return data

class StudentClassController:
    @staticmethod
    async def get_students_by_classroom(student_user_id: str):
        try:
            student = student_collection.find_one({"student_user_id": student_user_id})
            if not student:
                return {"error": "Student not found"}

            student["_id"] = str(student["_id"])

            classrooms_cursor = classroom_collection.find(
                {"students": str(student["_id"])},
                {
                    "_id": 1,
                    "classroom_name": 1,
                    "teacherId": 1
                }
            )

            classrooms = list(classrooms_cursor)

            if not classrooms:
                return {"message": "No classes found"}

           
            for classroom in classrooms:
                classroom["_id"] = str(classroom["_id"])
                classroom["teacherId"] = str(classroom["teacherId"])

            return classrooms

        except Exception as e:
            return {"error": str(e)}

        
    @staticmethod
    async def get_teacher_name(teacher_id: str):
        try:
            teacher = collection2.find_one({"_id": ObjectId(teacher_id)})

            if not teacher:
                return {"error": "Teacher not found"}

            return {
                "_id": str(teacher["_id"]),
                "name": teacher.get("name", "No name found")
            }

        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def get_teacher_name_by_userId(teacher_user_id:str):
        try:
            teaher= collection2.find_one({"teacher_user_id": teacher_user_id})
            if not teaher:
                return {"error": "Teacher not found"}
            return {
                "_id": str(teaher["_id"]),
                "name": teaher.get("name", "No name found")
            }       
        except Exception as e:
            return {
                "error": str(e)
            }
    
    @staticmethod
    async def get_classroom_name(classroom_id: str):
        try:
            classroom = classroom_collection.find_one({"_id": ObjectId(classroom_id)})

            if not classroom:
                return {"error": "Classroom not found"}

            return {
                "_id": str(classroom["_id"]),
                "classroom_name": classroom.get("classroom_name", "No classroom name found")
            }

        except Exception as e:
            return {"error": str(e)}
        
    @staticmethod
    async def get_time_table_by_student(student_id: str):
        try:
            student = student_collection.find_one({"student_user_id": student_id})
            if not student:
                return {"error": "Student not found"}

            student_id_str = str(student["_id"])

            classrooms = list(
                classroom_collection.find(
                    {"students": student_id_str},
                    {"_id": 1, "classroom_name": 1, "teacherId": 1}
                )
            )

            if not classrooms:
                return {"message": "No classes found"}

            time_tables = []

            for classroom in classrooms:
                classroom_id_str = str(classroom["_id"])

                time_table = Teacher_time_table_collection.find_one(
                    {"classroom_id": classroom_id_str}
                )

                if time_table:
                    time_tables.append(time_table)

          
            return serialize_mongo(time_tables)

        except Exception as e:
            traceback.print_exc()
            return {"error": str(e)}
    
    @staticmethod
    async def get_name_of_student_by_user_id(student_user_id: str):
        try:
            student = student_collection.find_one({"student_user_id": student_user_id})
            if not student:
                return {"error": "Student not found"}
            return {
                "_id": str(student["_id"]),
                "name": student.get("name", "No name found")
            }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_student_email_by_user_id(student_user_id: str):
        try:
            student = student_collection.find_one({"student_user_id": student_user_id})
            if not student:
                return {"error": "Student not found"}
            return {
                "_id": str(student["_id"]), 
                "email": student.get("email", "No email found")
            }
        except Exception as e:
            return {"error": str(e)}
        
    
    @staticmethod
    async def get_teacher_email_by_user_id(teacher_user_id: str):
        try:
            teacher = collection2.find_one({"teacher_user_id": teacher_user_id})
            if not teacher:
                return {"error": "Teacher not found"}
            return {
                "_id": str(teacher["_id"]), 
                "email": teacher.get("email", "No email found")
            }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_student_name_by_id(student_id: str):
        try:
            student = student_collection.find_one({"_id": ObjectId(student_id)})
            if not student:
                return {"error": "Student not found"}
            return {
                "_id": str(student["_id"]),
                "name": student.get("name", "No name found")
            }
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def get_student_ID_by_user_id(student_user_id: str):
            try:
                # Lookup student by your custom student_id field
                student = student_collection.find_one({"student_user_id": student_user_id})
                if not student:
                    return {"status": "error", "message": "Student not found"}

                # Return MongoDB ObjectId (_id) as string
                return {
                    "status": "success",
                    "_id": str(student["_id"]),  # Convert ObjectId to string for JSON
                    "student_id": student.get("student_id", "No student ID found")
                }

            except Exception as e:
                return {"status": "error", "message": str(e)}