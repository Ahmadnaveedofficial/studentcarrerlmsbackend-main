# from app.config.db import student_collection, admin_collection
# import string, hashlib, secrets, uuid, os
# from app.config.config import supabase
# import traceback
# from bson import ObjectId
# from app.models.studentSchema import changePasswordModel
# from app.routes.student.StudentGmail import send_email



# class AuthUtils:

#     @staticmethod
#     def generate_random_password(length: int = 8) -> str:
#         alphabet = string.ascii_letters + string.digits
#         return "".join(secrets.choice(alphabet) for _ in range(length))
# class StudentController:

#     @staticmethod
#     async def create_student(student, image):
#         try:
#             existing_student = student_collection.find_one({"email": student.email})
#             if existing_student:
#                 return {"message": "Student already registered in the portal"}

#             # ✅ SAME as teacher
#             raw_password = AuthUtils.generate_random_password()

#             image_url = None

#             # Upload image
#             if image:
#                 image_data = await image.read()
#                 image_name = f"{uuid.uuid4()}_{image.filename}"
#                 bucket_name = os.getenv("SUPABASE_BUCKET", "student_images")
#                 file_path = f"public/{image_name}"

#                 res = supabase.storage.from_(bucket_name).upload(
#                     file_path, image_data
#                 )

#                 if not res:
#                     raise Exception("Failed to upload image to Supabase")

#                 image_url = supabase.storage.from_(bucket_name).get_public_url(file_path)

#             # ✅ SAME as teacher
#             student_user = {
#                 "email": student.email,
#                 "password": raw_password,
#                 "role": "STUDENT",
#             }

#             result = admin_collection.insert_one(student_user)
#             student_user_id = str(result.inserted_id)

#             # ✅ SAME structure as teacher
#             new_student = {
#                 "name": student.name,
#                 "email": student.email,
#                 "password": raw_password,
#                 "student_user_id": student_user_id,  # 👈 FIXED (match teacher naming)
#                 "state": student.state,
#                 "Roll_Number": student.Roll_Number,
#                 "city": student.city,
#                 "address": student.address,
#                 "date_of_birth": student.date_of_birth,
#                 "phone_number": student.phone_number,
#                 "image_url": image_url
#             }

#             result = student_collection.insert_one(new_student)

#             # Send email (same style)
#             body = f"""
# Hello {student.name},

# 🎉 You have been successfully added!

# Login Details:
# Email: {student.email}
# Password: {raw_password}

# Please change your password after login.
# """

#             send_email(
#                 subject="Student Registration Successful",
#                 name="Admin",
#                 body=body,
#                 to_email=student.email,
#             )

#             return {
#                 "message": "Student added successfully.",
#                 "id": str(result.inserted_id),
#                 "password": raw_password,
#                 "image_url": image_url,
#             }

#         except Exception as e:
#             print(e, "Error in create_student")
#             traceback.print_exc()
#             return {"error": str(e)}
#     @staticmethod
#     async def all_student_fetch():
#         try:
#             students = list(student_collection.find())
#             for student in students:
#                 student["_id"] = str(student["_id"])
#             return students
#         except Exception as e:
#             return {"error": str(e)}
#     @staticmethod
#     async def student_detail(id: str):
#         try:
#             student = student_collection.find_one({"_id": ObjectId(id)})
#             student["_id"] = str(student["_id"])
#             return student
#         except Exception as e:
#             return {"error": str(e)}
#     @staticmethod
#     async def update_student_data(id: str, student: dict, image_url=None):
#         try:
        
#             if not isinstance(student, dict):
#                 student = student.dict()

           
#             if image_url:
#                 image_data = await image_url.read()
#                 import uuid, os
#                 from app.config.config import supabase

#                 image_name = f"{uuid.uuid4()}_{image_url.filename}"
#                 bucket_name = os.getenv("SUPABASE_BUCKET", "student_images")

#                 res = supabase.storage.from_(bucket_name).upload(
#                     f"public/{image_name}", image_data
#                 )
#                 if not res:
#                     raise Exception("Failed to upload image to Supabase")

#                 public_url = supabase.storage.from_(bucket_name).get_public_url(image_name)
#                 student["image_url"] = public_url

#             result = student_collection.update_one(
#                 {"_id": ObjectId(id)}, 
#                 {"$set": student}
#             )
#             if result.modified_count > 0:
#                 return {"message": "Student data updated successfully"}
#             else:
#                 return {"message": "Student not found"}
#         except Exception as e:
#             import traceback
#             print(e)
#             traceback.print_exc()
#             return {"error": str(e)}
#     @staticmethod
#     async def delete_student(id: str):
#         try:
#             student = student_collection.find_one({"_id": ObjectId(id)})

#             if not student:
#                 return {"message": "Student not found"}

#             student_collection.delete_one({"_id": ObjectId(id)})

#             if "student_user_id" in student:
#                 admin_collection.delete_one({
#                     "_id": ObjectId(student["student_user_id"])
#                 })

#             return {"message": "Student deleted from both collections successfully"}

#         except Exception as e:
#             return {"error": str(e)}
    
#     @staticmethod
#     async def change_student_password(studentChangePassword: changePasswordModel):
#         try:
#             raw_password = studentChangePassword.new_password

#             admin_user = admin_collection.find_one({
#                 "email": studentChangePassword.email,
#                 "role": "STUDENT"
#             })

#             if not admin_user:
#                 return {"message": "Student not found"}
#             admin_result = admin_collection.update_one(
#                 {
#                     "email": studentChangePassword.email,
#                     "role": "STUDENT"
#                 },
#                 {"$set": {"password": raw_password}}
#             )

#             # update student_collection
#             student_result = student_collection.update_one(
#                 {"email": studentChangePassword.email},
#                 {"$set": {"password": raw_password}}
#             )

#             if admin_result.matched_count > 0 and student_result.matched_count > 0:
#                 return {"message": "Password changed successfully"}

#             return {"message": "Password update failed"}

#         except Exception as e:
#             import traceback
#             traceback.print_exc()
#             return {"error": str(e)}

from app.config.db import student_collection, admin_collection
import string, hashlib, secrets, uuid, os
from app.config.config import supabase
import traceback
from bson import ObjectId
from app.models.studentSchema import changePasswordModel
from app.routes.student.StudentGmail import send_email
from app.utils.hash import hash_password



class AuthUtils:

    @staticmethod
    def generate_random_password(length: int = 8) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(secrets.choice(alphabet) for _ in range(length))
class StudentController:

    @staticmethod
    async def create_student(student, image):
        try:
            existing_student = student_collection.find_one({"email": student.email})
            if existing_student:
                return {"message": "Student already registered in the portal"}

            raw_password = AuthUtils.generate_random_password()

            image_url = None

            if image:
                image_data = await image.read()
                image_name = f"{uuid.uuid4()}_{image.filename}"
                bucket_name = os.getenv("SUPABASE_BUCKET", "student_images")
                file_path = f"public/{image_name}"

                res = supabase.storage.from_(bucket_name).upload(
                    file_path, image_data
                )

                if not res:
                    raise Exception("Failed to upload image to Supabase")

                image_url = supabase.storage.from_(bucket_name).get_public_url(file_path)

            # ✅ Login collection stores the HASHED password (used for /login verification)
            student_user = {
                "email": student.email,
                "password": hash_password(raw_password),
                "role": "STUDENT",
            }

            result = admin_collection.insert_one(student_user)
            student_user_id = str(result.inserted_id)

            new_student = {
                "name": student.name,
                "email": student.email,
                "password": raw_password,
                "student_user_id": student_user_id,
                "state": student.state,
                "Roll_Number": student.Roll_Number,
                "city": student.city,
                "address": student.address,
                "date_of_birth": student.date_of_birth,
                "phone_number": student.phone_number,
                "image_url": image_url
            }

            result = student_collection.insert_one(new_student)

            body = f"""
Hello {student.name},

🎉 You have been successfully added!

Login Details:
Email: {student.email}
Password: {raw_password}

Please change your password after login.
"""

            send_email(
                subject="Student Registration Successful",
                name="Admin",
                body=body,
                to_email=student.email,
            )

            return {
                "message": "Student added successfully.",
                "id": str(result.inserted_id),
                "password": raw_password,
                "image_url": image_url,
            }

        except Exception as e:
            print(e, "Error in create_student")
            traceback.print_exc()
            return {"error": str(e)}
    @staticmethod
    async def all_student_fetch():
        try:
            students = list(student_collection.find())
            for student in students:
                student["_id"] = str(student["_id"])
            return students
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def student_detail(id: str):
        try:
            student = student_collection.find_one({"_id": ObjectId(id)})
            student["_id"] = str(student["_id"])
            return student
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def update_student_data(id: str, student: dict, image_url=None):
        try:
        
            if not isinstance(student, dict):
                student = student.dict()

           
            if image_url:
                image_data = await image_url.read()
                import uuid, os
                from app.config.config import supabase

                image_name = f"{uuid.uuid4()}_{image_url.filename}"
                bucket_name = os.getenv("SUPABASE_BUCKET", "student_images")

                res = supabase.storage.from_(bucket_name).upload(
                    f"public/{image_name}", image_data
                )
                if not res:
                    raise Exception("Failed to upload image to Supabase")

                public_url = supabase.storage.from_(bucket_name).get_public_url(image_name)
                student["image_url"] = public_url

            result = student_collection.update_one(
                {"_id": ObjectId(id)}, 
                {"$set": student}
            )
            if result.modified_count > 0:
                return {"message": "Student data updated successfully"}
            else:
                return {"message": "Student not found"}
        except Exception as e:
            import traceback
            print(e)
            traceback.print_exc()
            return {"error": str(e)}
    @staticmethod
    async def delete_student(id: str):
        try:
            student = student_collection.find_one({"_id": ObjectId(id)})

            if not student:
                return {"message": "Student not found"}

            student_collection.delete_one({"_id": ObjectId(id)})

            if "student_user_id" in student:
                admin_collection.delete_one({
                    "_id": ObjectId(student["student_user_id"])
                })

            return {"message": "Student deleted from both collections successfully"}

        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def change_student_password(studentChangePassword: changePasswordModel):
        try:
            raw_password = studentChangePassword.new_password

            admin_user = admin_collection.find_one({
                "email": studentChangePassword.email,
                "role": "STUDENT"
            })

            if not admin_user:
                return {"message": "Student not found"}
            admin_result = admin_collection.update_one(
                {
                    "email": studentChangePassword.email,
                    "role": "STUDENT"
                },
                {"$set": {"password": hash_password(raw_password)}}
            )

            student_result = student_collection.update_one(
                {"email": studentChangePassword.email},
                {"$set": {"password": raw_password}}
            )

            if admin_result.matched_count > 0 and student_result.matched_count > 0:
                return {"message": "Password changed successfully"}

            return {"message": "Password update failed"}

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"error": str(e)}
