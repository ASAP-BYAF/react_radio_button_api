from sqlalchemy import join, outerjoin, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.task import Task
from api.models.appearing import Appearing, AppearingDetail
from api.models.file import File


async def get_all(db: AsyncSession) -> list[tuple[int, str, bool]]:
    result: Result = await db.execute(
        select(
            File.vol_num,
            File.file_num,
            Task.title,
            AppearingDetail.appearing_detail
        )
        .select_from(
            join(Appearing, Task, Task.id == Appearing.task_id)
            .join(AppearingDetail, AppearingDetail.id == Appearing.appearing_detail_id)
            .join(File, File.id == Appearing.file_id)
        )
        .order_by(File.vol_num, File.file_num)
    )
    return result.all()
