from fastapi import APIRouter, Depends, HTTPException
# from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.appearing_detail as appearing_detail_schema
import api.cruds.appearing_detail as appearing_detail_crud
from api.db import get_db

router = APIRouter()

# @router.post("/appearing_detail_title_by_vol_file", response_model=file_schema.FileCreateResponse)
# async def get_file_by_title(file_body: file_schema.FileBase, db: AsyncSession = Depends(get_db)):
#     print(file_body.vol_num)
#     print(file_body.file_num)
#     file = await file_crud.get_file_by_vol_file(db, file_body)
#     if file is None:
#         return JSONResponse(status_code=200, content={"message": "None"})
#     return file


@router.get("/appearings", response_model=list[appearing_detail_schema.AppearingDetailCreateResponse])
async def list_appearing(db: AsyncSession = Depends(get_db)):
    return await appearing_detail_crud.get_appearing_detail_all(db)


@router.post("/appearing_detail_create",
             response_model=appearing_detail_schema.AppearingDetailCreateResponse)
async def create_appearing(appearing_detail_body: appearing_detail_schema.AppearingDetailCreate,
                           db: AsyncSession = Depends(get_db)):
    return await appearing_detail_crud.create_appearing_detail(db, appearing_detail_body)


@router.post("/appearing_detail_by_name", response_model=appearing_detail_schema.AppearingDetailCreateResponse)
async def get_appearing_detail_by_name(appearing_detail_body: appearing_detail_schema.AppearingDetailBase, db: AsyncSession = Depends(get_db)):
    return await appearing_detail_crud.get_appearing_detail_by_name(db, appearing_detail_body.appearing_detail)


@router.delete("/appearing_delete", response_model=None)
async def delete_appearing_detail(appearing_detail_body: appearing_detail_schema.AppearingDetailBase, db: AsyncSession = Depends(get_db)):
    appearing_detail = await appearing_detail_crud.get_appearing_detail_by_name(db, appearing_detail_body.appearing_detail)
    if appearing_detail is None:
        raise HTTPException(status_code=404, detail="appearing_detail not found")
    return await appearing_detail_crud.delete_appearing_detail(db, original=appearing_detail)


@router.get("/appearing_id_min",
            response_model=appearing_detail_schema.AppearingDetailCreateResponse)
async def get_appearing_detail_id_min(db: AsyncSession = Depends(get_db)):
    return await appearing_detail_crud.get_appearing_detail_id_min(db)
