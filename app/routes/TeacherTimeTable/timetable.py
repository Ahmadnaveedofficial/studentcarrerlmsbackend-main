from fastapi import APIRouter
from app.config.db import Teacher_time_table_collection
from app.controllers.TeachertimeTable import TeachertimeTable
from app.models.TeacherTimeTableSchema import TimeSlot

router = APIRouter(
    tags=["Teacher Time Table"],
)
@router.post("/add_time_slot")
async def add_time_slot(time_slot: TimeSlot):
    return await TeachertimeTable.add_time_slot(time_slot)

@router.get("/teacher_time_table/{teacher_user_id}")
async def get_time_table_by_teacher(teacher_user_id: str):
    return await TeachertimeTable.get_time_table_by_teacher(teacher_user_id)

@router.put("/update_time_slot/{slot_id}")
async def update_time_slot(slot_id: str, updated_slot: TimeSlot):
    return await TeachertimeTable.update_time_slot(slot_id, updated_slot)

@router.delete("/delete_time_slot/{slot_id}")
async def delete_time_slot(slot_id: str):
    return await TeachertimeTable.delete_time_slot(slot_id)

@router.get("/all_time_slots")
async def get_all_time_slots():
    return await TeachertimeTable.get_all_time_slots()

@router.get("/time_table/{slot_id}")
async def get_time_table(slot_id: str):
    return await TeachertimeTable.get_time_table(slot_id)
