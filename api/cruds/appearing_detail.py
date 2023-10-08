from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.appearing as appearing_model
import api.schemas.appearing_detail as appearing_detail_schema


# async def get_file_by_vol_file(db: AsyncSession,
#                                file_base: file_schema.FileBase) -> file_model.File:
#     result: Result = await db.execute(
#         select(file_model.File)
#         .filter(file_model.File.vol_num == file_base.vol_num)
#         .filter(file_model.File.file_num == file_base.file_num)
#     )
#     return result.scalars().first()
async def get_appearing_detail_all(db: AsyncSession) -> list[tuple[int, str]]:
    result: Result = await db.execute(
        select(
            appearing_model.AppearingDetail.id,
            appearing_model.AppearingDetail.appearing_detail
        )
    )
    return result.all()


async def create_appearing_detail(db: AsyncSession,
                                  appearing_detail_create:
                                  appearing_detail_schema.
                                  AppearingDetailCreate) -> \
                                  appearing_model.AppearingDetail:
    appearing_detail = appearing_model \
                           .AppearingDetail(**appearing_detail_create.dict())
    db.add(appearing_detail)
    await db.commit()
    await db.refresh(appearing_detail)
    return appearing_detail


async def get_appearing_detail_by_name(db: AsyncSession,
                                appearing_detail_name: str)\
                             -> tuple[int, str]:
    print(appearing_detail_name)
    result: Result = await db.execute(
        select(appearing_model.AppearingDetail).filter(appearing_model.AppearingDetail.appearing_detail == appearing_detail_name)
    )
    return result.scalars().first()


async def delete_appearing_detail(db: AsyncSession, original: appearing_model.AppearingDetail) -> None:
    await db.delete(original)
    await db.commit()
