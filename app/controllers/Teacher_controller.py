# from app.config.db import collection2, admin_collection
# from app.config.config import supabase
# import string, hashlib, secrets, uuid, os
# import bcrypt
# import traceback
# from bson import ObjectId
# from app.models.TeacherSchema import TeacherModel,ChangePassword
# from app.routes.Teacher.TeacherGmail import send_email

# class AuthUtils:

#     @staticmethod
#     def generate_random_password(length: int = 8) -> str:
#         alphabet = string.ascii_letters + string.digits
#         return "".join(secrets.choice(alphabet) for _ in range(length))
# class TeacherController:
#     @staticmethod
#     async def create_teacher(teacher, image):
#         try:
#             existing_teacher = collection2.find_one({"email": teacher.email})
#             if existing_teacher:
#                 return {"message": "Teacher already registered"}

#             raw_password = AuthUtils.generate_random_password()

#             image_url = None

#             # Upload image
#             if image:
#                 image_data = await image.read()
#                 image_name = f"{uuid.uuid4()}_{image.filename}"
#                 bucket_name = os.getenv("SUPABASE_BUCKET", "teacher_images")
#                 file_path = f"public/{image_name}"

#                 res = supabase.storage.from_(bucket_name).upload(
#                     file_path, image_data
#                 )

#                 if not res:
#                     raise Exception("Image upload failed")

#                 image_url = supabase.storage.from_(bucket_name).get_public_url(file_path)

#             # ✅ Store plain password
#             teacher_user = {
#                 "email": teacher.email,
#                 "password": raw_password,  
#                 "role": "TEACHER",
#             }

#             result = admin_collection.insert_one(teacher_user)
#             teacher_user_id = str(result.inserted_id)

#             # Save teacher details
#             new_teacher = {
#                 "name": teacher.name,
#                 "email": teacher.email,
#                 "password": raw_password,
#                 "professionality": teacher.Teacher_Professionality,
#                 "status": "active",
#                 "Teacher_Designation": teacher.Teacher_Designation,
#                 "Teacher_Phone_Number": teacher.Teacher_Phone_Number,
#                 "image_url": image_url,
#                 "teacher_user_id": teacher_user_id,
#             }

#             registered_teacher = collection2.insert_one(new_teacher)

#             # Send email
#             body = f"""
# Hello {teacher.name},

# 🎉 You have been successfully added!

# Login Details:
# Email: {teacher.email}
# Password: {raw_password}

# Please change your password after login.
# """

#             send_email(
#                 subject="Teacher Registration Successful",
#                 name="Admin",
#                 body=body,
#                 to_email=teacher.email,
#             )

#             return {
#                 "message": "Teacher added successfully",
#                 "id": str(registered_teacher.inserted_id),
#                 "password": raw_password,
#                 "image_url": image_url,
#             }

#         except Exception as e:
#             print(e)
#             traceback.print_exc()
#             return {"error": str(e)}

#     # -------- Fetch teacher -------- #
#     @staticmethod
#     async def Teacher_detail(id: str):
#         try:
#             teacher = collection2.find_one({"_id": ObjectId(id)})
#             if teacher:
#                 teacher["_id"] = str(teacher["_id"])
#             return teacher
#         except Exception as e:
#             return {"error": str(e)}

#     # -------- Delete teacher -------- #
#     @staticmethod
#     async def delete_teacher(id: str):
                
#             teacher =  collection2.find_one({"_id": ObjectId(id)})

#             if not teacher:
#                 return {"message": "Teacher not found"}

#             collection2.delete_one({"_id": ObjectId(id)})

#             if "teacher_user_id" in teacher:
#                 admin_collection.delete_one({
#                     "_id": ObjectId(teacher["teacher_user_id"])
#                 })

#             return {"message": "Teacher deleted from both collections successfully"}

#     # -------- Update teacher -------- #
#     @staticmethod
#     async def update_Teacher(id: str, teacher: TeacherModel):
#         try:
#             result = collection2.update_one(
#                 {"_id": ObjectId(id)},
#                 {"$set": teacher.dict()}
#             )
#             if result.modified_count > 0:
#                 return {"message": "Teacher updated successfully"}
#             return {"message": "Teacher not found"}
#         except Exception as e:
#             return {"error": str(e)}

#     # -------- Get all teachers -------- #
#     @staticmethod
#     async def all_teacher_fetch():
#         try:
#             teachers = list(collection2.find())
#             for teacher in teachers:
#                 teacher["_id"] = str(teacher["_id"])
#             return teachers
#         except Exception as e:
#             return {"error": str(e)}

   
   
#     @staticmethod
#     async def change_teacher_password(TeacherChangePassword: ChangePassword):
#         try:
#             raw_password = TeacherChangePassword.new_password
#             email = TeacherChangePassword.email

#             user = admin_collection.find_one({
#                 "email": email,
#                 "role": "TEACHER"
#             })

#             if not user:
#                 return {"message": "Teacher not found in admin collection"}

#             teacher = collection2.find_one({"email": email})
#             if not teacher:
#                 return {"message": "Teacher record not found in teacher collection"}

        
#             admin_result = admin_collection.update_one(
#                 {"email": email, "role": "TEACHER"},
#                 {"$set": {"password": raw_password}}
#             )

#             teacher_result = collection2.update_one(
#                 {"email": email},
#                 {"$set": {"password": raw_password}}
#             )

#             if admin_result.modified_count > 0 or teacher_result.modified_count > 0:
#                 return {"message": "Password changed successfully"}

#             return {"message": "Password not updated"}

#         except Exception as e:
#             return {"error": str(e)}
        
    
#     @staticmethod
#     async def get_teacher_detail_by_userId(teacher_user_id: str):
#         try:
#             teacher = collection2.find_one({
#                 "teacher_user_id": teacher_user_id
#             })

#             if not teacher:
#                 return {"error": "Teacher not found"}

#             teacher["_id"] = str(teacher["_id"])

#             return teacher

#         except Exception as e:
#             return {"error": str(e)}




from app.config.db import collection2, admin_collection
from app.config.config import supabase
import string, hashlib, secrets, uuid, os
import bcrypt
import traceback
from bson import ObjectId
from app.models.TeacherSchema import TeacherModel,ChangePassword
from app.routes.Teacher.TeacherGmail import send_email
from app.utils.hash import hash_password

class AuthUtils:

    @staticmethod
    def generate_random_password(length: int = 8) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(secrets.choice(alphabet) for _ in range(length))
class TeacherController:
    @staticmethod
    async def create_teacher(teacher, image):
        try:
            existing_teacher = collection2.find_one({"email": teacher.email})
            if existing_teacher:
                return {"message": "Teacher already registered"}

            raw_password = AuthUtils.generate_random_password()

            image_url = None

            # Upload image
            if image:
                image_data = await image.read()
                image_name = f"{uuid.uuid4()}_{image.filename}"
                bucket_name = os.getenv("SUPABASE_BUCKET", "teacher_images")
                file_path = f"public/{image_name}"

                res = supabase.storage.from_(bucket_name).upload(
                    file_path, image_data
                )

                if not res:
                    raise Exception("Image upload failed")

                image_url = supabase.storage.from_(bucket_name).get_public_url(file_path)

            # ✅ Login collection stores the HASHED password (used for /login verification)
            teacher_user = {
                "email": teacher.email,
                "password": hash_password(raw_password),
                "role": "TEACHER",
            }

            result = admin_collection.insert_one(teacher_user)
            teacher_user_id = str(result.inserted_id)

            # Save teacher details (record copy keeps raw for admin visibility)
            new_teacher = {
                "name": teacher.name,
                "email": teacher.email,
                "password": raw_password,
                "professionality": teacher.Teacher_Professionality,
                "status": "active",
                "Teacher_Designation": teacher.Teacher_Designation,
                "Teacher_Phone_Number": teacher.Teacher_Phone_Number,
                "image_url": image_url,
                "teacher_user_id": teacher_user_id,
            }

            registered_teacher = collection2.insert_one(new_teacher)

            # Send email
            body = f"""
Hello {teacher.name},

🎉 You have been successfully added!

Login Details:
Email: {teacher.email}
Password: {raw_password}

Please change your password after login.
"""

            send_email(
                subject="Teacher Registration Successful",
                name="Admin",
                body=body,
                to_email=teacher.email,
            )

            return {
                "message": "Teacher added successfully",
                "id": str(registered_teacher.inserted_id),
                "password": raw_password,
                "image_url": image_url,
            }

        except Exception as e:
            print(e)
            traceback.print_exc()
            return {"error": str(e)}

    # -------- Fetch teacher -------- #
    @staticmethod
    async def Teacher_detail(id: str):
        try:
            teacher = collection2.find_one({"_id": ObjectId(id)})
            if teacher:
                teacher["_id"] = str(teacher["_id"])
            return teacher
        except Exception as e:
            return {"error": str(e)}

    # -------- Delete teacher -------- #
    @staticmethod
    async def delete_teacher(id: str):
                
            teacher =  collection2.find_one({"_id": ObjectId(id)})

            if not teacher:
                return {"message": "Teacher not found"}

            collection2.delete_one({"_id": ObjectId(id)})

            if "teacher_user_id" in teacher:
                admin_collection.delete_one({
                    "_id": ObjectId(teacher["teacher_user_id"])
                })

            return {"message": "Teacher deleted from both collections successfully"}

    # -------- Update teacher -------- #
    @staticmethod
    async def update_Teacher(id: str, teacher: TeacherModel):
        try:
            result = collection2.update_one(
                {"_id": ObjectId(id)},
                {"$set": teacher.dict()}
            )
            if result.modified_count > 0:
                return {"message": "Teacher updated successfully"}
            return {"message": "Teacher not found"}
        except Exception as e:
            return {"error": str(e)}

    # -------- Get all teachers -------- #
    @staticmethod
    async def all_teacher_fetch():
        try:
            teachers = list(collection2.find())
            for teacher in teachers:
                teacher["_id"] = str(teacher["_id"])
            return teachers
        except Exception as e:
            return {"error": str(e)}

   
   
    @staticmethod
    async def change_teacher_password(TeacherChangePassword: ChangePassword):
        try:
            raw_password = TeacherChangePassword.new_password
            email = TeacherChangePassword.email

            user = admin_collection.find_one({
                "email": email,
                "role": "TEACHER"
            })

            if not user:
                return {"message": "Teacher not found in admin collection"}

            teacher = collection2.find_one({"email": email})
            if not teacher:
                return {"message": "Teacher record not found in teacher collection"}

        
            admin_result = admin_collection.update_one(
                {"email": email, "role": "TEACHER"},
                {"$set": {"password": hash_password(raw_password)}}
            )

            teacher_result = collection2.update_one(
                {"email": email},
                {"$set": {"password": raw_password}}
            )

            if admin_result.modified_count > 0 or teacher_result.modified_count > 0:
                return {"message": "Password changed successfully"}

            return {"message": "Password not updated"}

        except Exception as e:
            return {"error": str(e)}
        
    
    @staticmethod
    async def get_teacher_detail_by_userId(teacher_user_id: str):
        try:
            teacher = collection2.find_one({
                "teacher_user_id": teacher_user_id
            })

            if not teacher:
                return {"error": "Teacher not found"}

            teacher["_id"] = str(teacher["_id"])

            return teacher

        except Exception as e:
            return {"error": str(e)}