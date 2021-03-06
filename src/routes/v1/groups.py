from typing import Optional

from fastapi import APIRouter

from src.controllers.group_controller import get_all_groups, is_group_exists
from src.schemas.schema import x_schedule_header
from src.utils.events import Events
from src.utils.tracking import track

tag = "Groups"
router = APIRouter()


@router.get("", tags=[tag])
@track(fmt="query={query}, faculty={faculty}", event=Events.GET_ALL_GROUPS)
async def groups(
    *,
    query: Optional[str] = None,
    faculty: Optional[int] = None,
    schedule_url: str = x_schedule_header
):
    return await get_all_groups(schedule_url=schedule_url, faculty=faculty, query=query)


@router.get("/exists", tags=[tag])
@track(fmt="query={query}, faculty={faculty}", event=Events.IS_GROUP_EXISTS)
async def group_exists(
    *, query: str, faculty: Optional[str] = None, schedule_url: str = x_schedule_header
):
    return await is_group_exists(
        schedule_url=schedule_url, group=query, faculty=faculty
    )
