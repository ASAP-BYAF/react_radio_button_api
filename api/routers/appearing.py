from fastapi import APIRouter, Depends, HTTPException
# from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.appearing as appearing_schema
import api.cruds.appearing as appearing_crud
from api.db import get_db

router = APIRouter()

# @router.post("/file_title_by_vol_file", response_model=file_schema.FileCreateResponse)
# async def get_file_by_title(file_body: file_schema.FileBase, db: AsyncSession = Depends(get_db)):
#     print(file_body.vol_num)
#     print(file_body.file_num)
#     file = await file_crud.get_file_by_vol_file(db, file_body)
#     if file is None:
#         return JSONResponse(status_code=200, content={"message": "None"})
#     return file


@router.post("/appearing_create",
             response_model=appearing_schema.AppearingCreateResponse)
async def create_appearing(appearing_body: appearing_schema.AppearingCreate,
                           db: AsyncSession = Depends(get_db)):
    
    # 既に登録されている場合は登録できない。
    appearing = await appearing_crud.get_appearing(
        db, file_id=appearing_body.file_id, task_id=appearing_body.task_id
        )
    if not appearing is None:
        raise HTTPException(status_code=422, detail="Appearing already exist")
    return await appearing_crud.create_appearing(db, appearing_body)


@router.put("/appearing_update", response_model=appearing_schema.AppearingCreateResponse)
async def update_appearing(appearing_body: appearing_schema.AppearingBase, db: AsyncSession = Depends(get_db)):
    file_id = appearing_body.file_id
    task_id = appearing_body.task_id
    appearing = await appearing_crud.get_appearing(db, file_id=file_id, task_id=task_id)
    if appearing is None:
        raise HTTPException(status_code=404, detail="Appearing not found")
    return await appearing_crud.update_appearing(db, appearing_body, original=appearing)


@router.get("/appearing_with_file_id/{file_id}", response_model=list[appearing_schema.AppearingBase])
async def list_appearings(file_id: int, db: AsyncSession = Depends(get_db)):
    return await appearing_crud.get_appearing_with_file_id(db, file_id)


@router.delete("/appearing_delete/", response_model=None)
async def delete_appearing(appearing_body: appearing_schema.AppearingDelete, db: AsyncSession = Depends(get_db)):
    file_id = appearing_body.file_id
    task_id = appearing_body.task_id
    appearing = await appearing_crud.get_appearing(db, file_id=file_id, task_id=task_id)
    if appearing is None:
        raise HTTPException(status_code=404, detail="Appearing not found")
    return await appearing_crud.delete_appearing(db, original=appearing)
