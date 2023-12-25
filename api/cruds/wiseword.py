from sqlalchemy import select, join
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.wiseword as wiseword_schema
from api.models.wiseword import Wiseword
from api.models.task import Task
from api.models.appearing import Appearing, AppearingDetail
from api.models.file import File


async def get_wisewords_all(db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            Wiseword.id,
            Wiseword.phrase,
            Task.title,
            File.vol_num,
            File.file_num,
        )
        .select_from(
            join(Wiseword, Task, Task.id == Wiseword.task_id)
            .join(File, File.id == Wiseword.file_id)
        )
    )
    return result.all()

async def get_wiseword(wiseword_id: int, db: AsyncSession) -> tuple[int, str]:
    result: Result = await db.execute(
        select(
            Wiseword.id,
            Wiseword.phrase,
            Task.title,
            File.vol_num,
            File.file_num,
        )
        .select_from(
            join(Wiseword, Task, Task.id == Wiseword.task_id)
            .join(File, File.id == Wiseword.file_id)
        )
        .filter(Wiseword.id == wiseword_id)

    )
    return result.scalars().first()

async def get_wisewords_by_file_id(file_id: int, db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            Wiseword.id,
            Wiseword.phrase,
            Task.title,
            File.vol_num,
            File.file_num,
        )
        .select_from(
            join(Wiseword, Task, Task.id == Wiseword.task_id)
            .join(File, File.id == Wiseword.file_id)
        )
        .filter(Wiseword.file_id == file_id)
    )
    return result.all()


async def get_wisewords_by_task_id(task_id: int, db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            Wiseword.id,
            Wiseword.phrase,
            Task.title,
            File.vol_num,
            File.file_num,
        )
        .select_from(
            join(Wiseword, Task, Task.id == Wiseword.task_id)
            .join(File, File.id == Wiseword.file_id)
        )
        .filter(Wiseword.task_id == task_id)
    )
    return result.all()


async def create_wiseword(wiseword_create: wiseword_schema.WisewordCreate, db: AsyncSession) \
    -> Wiseword:
    wiseword = Wiseword(**wiseword_create.dict())
    db.add(wiseword)
    await db.commit()
    await db.refresh(wiseword)
    return wiseword


async def update_wiseword( 
    wiseword_create: wiseword_schema.WisewordBase,
    original: Wiseword,
    db: AsyncSession
) -> Wiseword:
    original.phrase = wiseword_create.phrase
    original.task_id = wiseword_create.task_id
    original.file_id = wiseword_create.file_id
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_wiseword(original: Wiseword, db: AsyncSession) -> None:
    await db.delete(original)
    await db.commit()