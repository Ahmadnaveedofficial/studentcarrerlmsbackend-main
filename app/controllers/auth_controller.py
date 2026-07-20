# from app.config.db import admin_collection
# from app.models.adminSchema import Admin, LoginSchema
# from app.utils.hash import hash_password
# from app.utils.hash import verify_password
# from app.utils.jwt_handler import create_access_token

# class AuthControllers:
#     @staticmethod
#     async def admin_panel(admin: Admin):
#             hashed_password = hash_password(
#             admin.password
#         )

#             new_admin = {
#                 "email": admin.email,
#                 "password": hashed_password,
#                 "role": admin.role
#             }

#             result = admin_collection.insert_one(
#                 new_admin
#             )

#             return {
#                 "message": "Admin Registered Successfully",
#                 "id": str(result.inserted_id)
#             }
    
#     @staticmethod
#     async def admin_login(user: LoginSchema):

#         admin = admin_collection.find_one({
#             "email": user.email,
#             "password": user.password
#         })

#         if not admin:

#             return {
#                 "error": "Invalid email or password"
#             }

#         admin["_id"] = str(admin["_id"])

#         # CREATE JWT TOKEN
#         access_token = create_access_token({
#             "id": admin["_id"],
#             "email": admin["email"],
#             "role": admin["role"]
#         })

#         return {

#             "message": "Login Successful",

#             "access_token": access_token,

#             "token_type": "bearer",

#             "user": {

#                 "_id": admin["_id"],
#                 "email": admin["email"],
#                 "role": admin["role"]
#             }
#         }






from app.config.db import admin_collection
from app.models.adminSchema import Admin, LoginSchema
from app.utils.hash import hash_password
from app.utils.hash import verify_password
from app.utils.jwt_handler import create_access_token

class AuthControllers:
    @staticmethod
    async def admin_panel(admin: Admin):
            hashed_password = hash_password(
            admin.password
        )

            new_admin = {
                "email": admin.email,
                "password": hashed_password,
                "role": admin.role
            }

            result = admin_collection.insert_one(
                new_admin
            )

            return {
                "message": "Admin Registered Successfully",
                "id": str(result.inserted_id)
            }
    
    @staticmethod
    async def admin_login(user: LoginSchema):

        admin = admin_collection.find_one({
            "email": user.email
        })

        if not admin or not verify_password(user.password, admin["password"]):

            return {
                "error": "Invalid email or password"
            }

        admin["_id"] = str(admin["_id"])

        # CREATE JWT TOKEN
        access_token = create_access_token({
            "id": admin["_id"],
            "email": admin["email"],
            "role": admin["role"]
        })

        return {

            "message": "Login Successful",

            "access_token": access_token,

            "token_type": "bearer",

            "user": {

                "_id": admin["_id"],
                "email": admin["email"],
                "role": admin["role"]
            }
        }