from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.file as file_schema
import api.cruds.file as file_crud
from api.db import get_db

router = APIRouter()


@router.post("/file_name_by_vol_file",
             response_model=file_schema.FileCreateResponse)
async def get_name_by_vol_file_num(file_body: file_schema.FileBase, db: AsyncSession = Depends(get_db)):
    print(file_body.vol_num)
    print(file_body.file_num)
    file = await file_crud.get_name_by_vol_file_num(db, file_body)
    if file is None:
        return JSONResponse(status_code=200, content={"message": "None"})
    return file


@router.post("/file_create", response_model=file_schema.FileCreateResponse)
async def create_file(file_body: file_schema.FileCreate, db: AsyncSession = Depends(get_db)):
    return await file_crud.create_file(db, file_body)


@router.post("/file_by_name", response_model=file_schema.FileCreateResponse)
async def get_file_by_name(file_body: file_schema.FileSerachByName, db: AsyncSession = Depends(get_db)):
    return await file_crud.get_file_by_name(db, file_body)