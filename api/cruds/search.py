from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.models.appearing as appearing_model


async def get_all(db: AsyncSession) -> list[tuple[int, str, bool]]:
    result: Result = await db.execute(
        select(
            appearing_model.Appearing.file_id,
            appearing_model.Appearing.task_id,
            appearing_model.Appearing.appearing_detail_id,
        )
    )
    return result.all()
