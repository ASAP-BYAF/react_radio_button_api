from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.file as file_model
import api.schemas.file as file_schema


async def get_name_by_vol_file_num(db: AsyncSession,
                               file_base: file_schema.FileBase) -> file_model.File:
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


async def get_file_by_name(db: AsyncSession,
                           file_name: str)\
                             -> tuple[int, str]:
    print(file_name)
    result: Result = await db.execute(
        select(file_model.File).filter(file_model.File.file_name == file_name)
    )
    return result.scalars().first()


async def get_file_by_id(db: AsyncSession,
                         file_id: int)\
                             -> tuple[int, str]:
    print(file_id)
    result: Result = await db.execute(
        select(file_model.File).filter(file_model.File.id == file_id)
    )
    return result.scalars().first()


async def update_file(
    db: AsyncSession, file_create: file_schema.FileCreate, original: file_model.File
) -> file_model.File:
    original.file_name = file_create.file_name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def get_previous_file_id(
    db: AsyncSession
) -> file_model.File:
    result: Result = await db.execute(
        select(
            file_model.File.id
            )
            .order_by(file_model.File.vol_num, file_model.File.file_num)
    )
    return result.all()
