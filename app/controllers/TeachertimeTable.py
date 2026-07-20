from app.config.db import Teacher_time_table_collection,classroom_collection,admin_collection,collection2
from app.models.TeacherTimeTableSchema import TimeSlot
from bson import ObjectId

class TeachertimeTable:
    @staticmethod
    async def add_time_slot(time_slot: TimeSlot):
        try:
            timeS= {
                "day": time_slot.day,
                "start_time": time_slot.start_time.strftime("%H:%M:%S"),
                "end_time": time_slot.end_time.strftime("%H:%M:%S"),
                "teacher_id": time_slot.teacher_id,
                "classroom_id": time_slot.classroom_id,
                "roomno": time_slot.roomno,
                "date": time_slot.date
            }
            result= Teacher_time_table_collection.insert_one(timeS)
            return {"message": "Time slot added successfully", "id": str(result.inserted_id)}
            
            
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    async def get_time_table_by_teacher(teacher_user_id: str):
        try:
            teacher= collection2.find_one({"teacher_user_id": teacher_user_id})
            if not teacher:
                return {"error": "Teacher not found"}
            teacher_id= str(teacher["_id"])
            time_slots= list(Teacher_time_table_collection.find({"teacher_id": teacher_id}))
            for slot in time_slots:
                slot["_id"]= str(slot["_id"])
                slot["teacher_id"]= str(slot["teacher_id"])
                slot["classroom_id"]= str(slot["classroom_id"])
            return time_slots
        except Exception as e:
            return {"error": str(e)}
        
    @staticmethod
    async def update_time_slot(slot_id: str, updated_slot: TimeSlot):
        try:
            update_data= {
                "day": updated_slot.day,
                "start_time": updated_slot.start_time.strftime("%H:%M:%S"),
                "end_time": updated_slot.end_time.strftime("%H:%M:%S"),
                "teacher_id": updated_slot.teacher_id,
                "date": updated_slot.date,
                "roomno": updated_slot.roomno,
                "classroom_id": updated_slot.classroom_id
            }
            result= Teacher_time_table_collection.update_one(
                {"_id": ObjectId(slot_id)},
                {"$set": update_data}
            )
            if result.matched_count == 0:
                return {"error": "Time slot not found"}
            return {"message": "Time slot updated successfully"}
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def delete_time_slot(slot_id: str):
        try:
            result= Teacher_time_table_collection.delete_one({"_id": ObjectId(slot_id)})
            if result.deleted_count == 0:
                return {"error": "Time slot not found"}
            return {"message": "Time slot deleted successfully"}
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def get_all_time_slots():
        try:
            time_slots= list(Teacher_time_table_collection.find())
            for slot in time_slots:
                slot["_id"]= str(slot["_id"])
                slot["teacher_id"]= str(slot["teacher_id"])
                slot["classroom_id"]= str(slot["classroom_id"])
            return time_slots
        except Exception as e:
            return {"error": str(e)}
    @staticmethod
    async def get_time_table(slot_id: str):
        try:
            if not ObjectId.is_valid(slot_id):
                return {"error": "Invalid slot ID format"}
            slot = Teacher_time_table_collection.find_one(
                {"_id": ObjectId(slot_id)}
            )
            if not slot:
                return {"error": "Time slot not found"}
            slot["_id"] = str(slot["_id"])
            slot["day"] = str(slot.get("day", ""))
            slot["start_time"] = str(slot.get("start_time", ""))
            slot["end_time"] = str(slot.get("end_time", ""))
            slot["teacher_id"] = str(slot.get("teacher_id", ""))
            slot["date"] = str(slot.get("date", ""))
            slot["roomno"] = str(slot.get("roomno", ""))
            slot["classroom_id"] = str(slot.get("classroom_id", ""))
            return slot
        except Exception as e:
            return {"error": str(e)}
