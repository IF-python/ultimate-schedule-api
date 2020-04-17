from typing import Optional

from fastapi import APIRouter

from src.controllers.teacher_controller import get_all_teachers, is_teacher_exists
from src.schemas.schema import x_schedule_header

tag = "Teachers"
router = APIRouter()


@router.get("", tags=[tag])
async def teacher(*, query: Optional[str] = None, faculty: Optional[int] = None, schedule_url: str = x_schedule_header):
    return await get_all_teachers(schedule_url=schedule_url, faculty=faculty, query=query)


@router.get("/exists", tags=[tag])
async def teacher_exists(
        *, query: Optional[str] = None,
        faculty: Optional[int] = None, schedule_url: str = x_schedule_header
):
    return await is_teacher_exists(schedule_url=schedule_url, teacher=query, faculty=faculty)