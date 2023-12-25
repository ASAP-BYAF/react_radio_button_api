from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.schemas.wiseword as wiseword_schema
import api.cruds.wiseword as wiseword_crud

router = APIRouter()


@router.get("/wisewords_all", response_model=list[wiseword_schema.WisewordGetResponse])
async def wisewords(db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.get_wisewords_all(db)


@router.get("/wiseword/{word_id}", response_model=wiseword_schema.WisewordCreateResponse)
async def wiseword(word_id, db: AsyncSession = Depends(get_db)):
    wiseword = await wiseword_crud.get_wiseword(int(word_id), db)
    if wiseword is None:
        raise HTTPException(status_code=404, detail="wiseword not found")
    return wiseword


@router.get("/wisewords_by_file_id/{file_id}", response_model=list[wiseword_schema.WisewordGetResponse])
async def wisewords(file_id, db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.get_wisewords_by_file_id(int(file_id), db)


@router.get("/wisewords_by_task_id/{task_id}", response_model=list[wiseword_schema.WisewordGetResponse])
async def wisewords(task_id, db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.get_wisewords_by_task_id(int(task_id), db)


@router.post("/wiseword_create", response_model=wiseword_schema.WisewordCreateResponse)
async def create_wiseword(wiseword_body: wiseword_schema.WisewordCreate, db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.create_wiseword(wiseword_body, db)


@router.put("/wiseword_update/{word_id}", response_model=wiseword_schema.WisewordCreateResponse)
async def update_wiseword( word_id: int, wiseword_body: wiseword_schema.WisewordCreate, db: AsyncSession = Depends(get_db) ):
    wiseword = await wiseword_crud.get_wiseword( int(word_id), db )
    if wiseword is None:
        raise HTTPException(status_code=404, detail="wiseword not found")
    return await wiseword_crud.update_wiseword(wiseword_body, original=wiseword, db=db)


@router.delete("/wiseword_delete/{word_id}", response_model=None)
async def delete_wiseword(word_id, db: AsyncSession = Depends(get_db)):
    wiseword = await wiseword_crud.get_wiseword(int(word_id), db)
    if wiseword is None:
        raise HTTPException(status_code=404, detail="wiseword not found")
    return await wiseword_crud.delete_wiseword(original=wiseword, db=db)
