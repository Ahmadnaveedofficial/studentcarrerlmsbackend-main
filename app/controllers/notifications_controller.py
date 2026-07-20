from app.models.notifications_model import Notification
from app.config.db import notifications
from bson import ObjectId


class NotificationController:

    @staticmethod
    def create_notification(data: Notification):
        try:

            notification_dict = data.dict()

            result =  notifications.insert_one(notification_dict)

            return {
                "message": "Notification created",
                "id": str(result.inserted_id)
            }
        except Exception as e:
            return {
                "error": str(e)
            }
        
    

    @staticmethod
    def get_teacher_notifications(teacher_id: str):
        try:
            notification_list = []

            cursor = notifications.find({
            "teacher_id": teacher_id
           })

            for notification in cursor:

                notification["_id"] = str(notification["_id"])

                notification_list.append(notification)

            return notification_list
        except Exception as e:
            return {
                "error": str(e)
            }
            

        