from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.wiseword as wiseword_model
import api.schemas.wiseword as wiseword_schema


async def get_wisewords_all(db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            wiseword_model.Wiseword.phrase,
            wiseword_model.Wiseword.file_id,
            wiseword_model.Wiseword.id,
        )
    )
    return result.all()

async def get_wiseword(wiseword_id: int, db: AsyncSession) -> tuple[int, str]:
    result: Result = await db.execute(
        select(
            wiseword_model.Wiseword
        ).filter(wiseword_model.Wiseword.id == wiseword_id)
    )
    return result.scalars().first()

async def get_wisewords_by_file_id(file_id: int, db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            wiseword_model.Wiseword.phrase,
            wiseword_model.Wiseword.file_id,
            wiseword_model.Wiseword.id,
        ).filter(wiseword_model.Wiseword.file_id == file_id)
    )
    return result.all()


async def create_wiseword(wiseword_create: wiseword_schema.WisewordCreate, db: AsyncSession) \
    -> wiseword_model.Wiseword:
    wiseword = wiseword_model.Wiseword(**wiseword_create.dict())
    db.add(wiseword)
    await db.commit()
    await db.refresh(wiseword)
    return wiseword


async def update_wiseword( 
    wiseword_create: wiseword_schema.WisewordBase,
    original: wiseword_model.Wiseword,
    db: AsyncSession
) -> wiseword_model.Wiseword:
    original.phrase = wiseword_create.phrase
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_wiseword(original: wiseword_model.Wiseword, db: AsyncSession) -> None:
    await db.delete(original)
    await db.commit()