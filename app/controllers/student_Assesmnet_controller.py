# from bson import ObjectId

# from app.config.db import student_collection, classroom_collection, assesment_collection


# class Assesment:

#     @staticmethod
#     def fetch_assement_by_student_userid(user_id: str):
#         try:
#             student = student_collection.find_one({
#                 "student_id": user_id
#             })

#             if not student:
#                 return {"message": "Student not found"}
#             student_object_id_str = str(student["_id"])

#             classrooms = classroom_collection.find({
#                 "students": student_object_id_str
#             })

#             class_ids = []
#             for classroom in classrooms:
#                 class_ids.append(classroom["_id"])  
#             if not class_ids:
#                 return []
#             assesments_cursor = assesment_collection.find({
#                 "classId": {"$in": class_ids}
#             })

#             assesments = []
#             for assesment in assesments_cursor:
#                 assesment["_id"] = str(assesment["_id"])
#                 assesment["classId"] = str(assesment["classId"])
#                 assesments.append(assesment)

#             return assesments
#         except Exception as e:
#             return {
#                 "message": "An error occurred while fetching assessments",
#                 "error": str(e)
#             }
    
#     @staticmethod
#     async def get_assesment_by_id(assesmentId:str):
#         try:
#             assesment = assesment_collection.find_one({
#                 "_id": ObjectId(assesmentId)
#             })
#             if not assesment:
#                 return {"message": "Assesment not found"}
#             assesment["_id"] = str(assesment["_id"])
#             assesment["name"] = str(assesment["name"])
#             assesment["description"] = str(assesment["description"])
#             assesment["created_at"] = str(assesment["created_at"])
#             assesment["classId"] = str(assesment["classId"])
            
#             return assesment
#         except Exception as e:
#             return {
#                 "message": "An error occurred while fetching the assessment",
#                 "error": str(e)
#             }





from bson import ObjectId

from app.config.db import student_collection, classroom_collection, assesment_collection


class Assesment:

    @staticmethod
    def fetch_assement_by_student_userid(user_id: str):
        try:
            student = student_collection.find_one({
                "student_user_id": user_id
            })

            if not student:
                return {"message": "Student not found"}
            student_object_id_str = str(student["_id"])

            classrooms = classroom_collection.find({
                "students": student_object_id_str
            })

            class_ids = []
            for classroom in classrooms:
                class_ids.append(classroom["_id"])  
            if not class_ids:
                return []
            assesments_cursor = assesment_collection.find({
                "classId": {"$in": class_ids}
            })

            assesments = []
            for assesment in assesments_cursor:
                assesment["_id"] = str(assesment["_id"])
                assesment["classId"] = str(assesment["classId"])
                assesments.append(assesment)

            return assesments
        except Exception as e:
            return {
                "message": "An error occurred while fetching assessments",
                "error": str(e)
            }
    
    @staticmethod
    async def get_assesment_by_id(assesmentId:str):
        try:
            assesment = assesment_collection.find_one({
                "_id": ObjectId(assesmentId)
            })
            if not assesment:
                return {"message": "Assesment not found"}
            assesment["_id"] = str(assesment["_id"])
            assesment["name"] = str(assesment["name"])
            assesment["description"] = str(assesment["description"])
            assesment["created_at"] = str(assesment["created_at"])
            assesment["classId"] = str(assesment["classId"])
            
            return assesment
        except Exception as e:
            return {
                "message": "An error occurred while fetching the assessment",
                "error": str(e)
            }