from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.appearing as appearing_model
import api.schemas.appearing as appearing_schema


# async def get_file_by_vol_file(db: AsyncSession,
#                                file_base: file_schema.FileBase) -> file_model.File:
#     result: Result = await db.execute(
#         select(file_model.File)
#         .filter(file_model.File.vol_num == file_base.vol_num)
#         .filter(file_model.File.file_num == file_base.file_num)
#     )
#     return result.scalars().first()


async def create_appearing(db: AsyncSession,
                           appearing_create: appearing_schema.AppearingCreate) -> appearing_model.Appearing:
    appearing = appearing_model.Appearing(**appearing_create.dict())
    db.add(appearing)
    await db.commit()
    await db.refresh(appearing)
    return appearing


async def get_appearing(db: AsyncSession, file_id: int, task_id: int) -> appearing_model.Appearing | None:
    result: Result = await db.execute(
        select(appearing_model.Appearing).filter(appearing_model.Appearing.file_id == file_id, appearing_model.Appearing.task_id == task_id)
    )
    return result.scalars().first()


async def update_appearing(
    db: AsyncSession, appearing_create: appearing_schema.AppearingCreate, original: appearing_model.Appearing
) -> appearing_model.Appearing:
    original.appearing_detail_id = appearing_create.appearing_detail_id
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def get_appearing_with_file_id(db: AsyncSession, file_id: int) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            appearing_model.Appearing.file_id,
            appearing_model.Appearing.task_id,
            appearing_model.Appearing.appearing_detail_id,
        ).filter(appearing_model.Appearing.file_id == file_id)
    )
    return result.all()
