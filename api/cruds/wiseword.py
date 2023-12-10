from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.wiseword as wiseword_model
import api.schemas.wiseword as wiseword_schema


async def get_wisewords_all(db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            wiseword_model.Wiseword.id,
            wiseword_model.Wiseword.phrase
        )
    )
    return result.all()

async def get_wiseword(wiseword_id: int, db: AsyncSession) -> tuple[int, str]:
    result: Result = await db.execute(
        select(
            wiseword_model.Wiseword.id,
            wiseword_model.Wiseword.phrase
        ).filter(wiseword_model.Wiseword.id == wiseword_id)
    )
    return result.scalars().first()

async def get_wisewords_by_file_id(file_id: int, db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            wiseword_model.Wiseword.id,
            wiseword_model.Wiseword.phrase
        ).filter(wiseword_model.Wiseword.file_id == file_id)
    )
    return result
