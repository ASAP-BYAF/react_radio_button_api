from fastapi import APIRouter, Depends, HTTPException
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
    return await file_crud.get_file_by_name(db, file_body.file_name)


@router.put("/file_update/{file_id}", response_model=file_schema.FileCreateResponse)
async def update_file(file_id: int, file_body: file_schema.FileCreate, db: AsyncSession = Depends(get_db)):
    file = await file_crud.get_file_by_id(db, file_id=file_id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return await file_crud.update_file(db, file_body, original=file)


@router.get("/file_by_id/{file_id}", response_model=file_schema.FileCreateResponse)
async def get_file_by_id(file_id: int, db: AsyncSession = Depends(get_db)):
    file = await file_crud.get_file_by_id(db, file_id=file_id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file


@router.get("/previous_file_id/{file_id}", response_model=file_schema.FileId)
async def get_previous_file_id(file_id: int, db: AsyncSession = Depends(get_db)):
    
    # file_id に対応するファイルが存在していない時はエラーを返す。
    file = await file_crud.get_file_by_id(db, file_id=file_id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    file_id_list = await file_crud.get_previous_file_id(db)
    
    previous_file_id = -1
    for i_file_id in file_id_list:
        if (i_file_id := i_file_id[0]) == file_id:
            break
        else:
            previous_file_id = i_file_id

    # 初めてファイルを作った時あるいは file1 の登録時は直前のファイルが存在していない。
    if previous_file_id < 0:
        raise HTTPException(status_code=404, detail="Previous file not found")
    return {"file_id": previous_file_id}
