from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.file as file_model
import api.schemas.file as file_schema

async def get_file_by_vol_file(db: AsyncSession, file_base: file_schema.FileBase) -> file_model.File:
    result: Result = await db.execute(
        select(file_model.File)
        .filter(file_model.File.vol_num == file_base.vol_num)
        .filter(file_model.File.file_num == file_base.file_num)
    )
    return result.scalars().first()

async def create_file(db: AsyncSession, file_create: file_schema.FileCreate) -> file_model.File:
    file = file_model.File(**file_create.dict())
    db.add(file)
    await db.commit()
    await db.refresh(file)
    return file