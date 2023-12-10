from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.schemas.wiseword as wiseword_schema
import api.cruds.wiseword as wiseword_crud

router = APIRouter()


@router.get("/wisewords", response_model=list[wiseword_schema.WisewordCreateResponse])
async def wisewords(db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.get_wisewords_all(db)


@router.get("/wiseword/{word_id}", response_model=wiseword_schema.WisewordCreateResponse)
async def wiseword(word_id, db: AsyncSession = Depends(get_db)):
    wiseword = await wiseword_crud.get_wiseword(int(word_id), db)
    if wiseword is None:
        raise HTTPException(status_code=404, detail="wiseword not found")
    return wiseword


@router.get("/wisewords/{file_id}", response_model=list[wiseword_schema.WisewordCreateResponse])
async def wisewords(file_id, db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.get_wisewords_by_file_id(int(file_id), db)


@router.post("/appearing_detail_create",
             response_model=wiseword_schema.WisewordCreateResponse)
async def create_appearing(appearing_detail_body: wiseword_schema.WisewordCreate,
                           db: AsyncSession = Depends(get_db)):
    return await wiseword_crud.create_appearing_detail(db, appearing_detail_body)


@router.put("/update_appearing_detail/{appearing_detail_id}", response_model=wiseword_schema.WisewordCreateResponse)
async def update_appearing_detail(
        appearing_detail_id: int,
        appearing_detail_body: wiseword_schema.WisewordBase,
        db: AsyncSession = Depends(get_db)
    ):
    appearing_detail = await wiseword_crud \
        .get_appearing_detail_by_id(
            db,
            appearing_detail_id=appearing_detail_id
        )
    if appearing_detail is None:
        raise HTTPException(status_code=404, detail="appearing_detail not found")
    return await wiseword_crud.update_appearing_detail(db, appearing_detail_body, original=appearing_detail)


@router.delete("/appearing_detail_delete", response_model=None)
async def delete_appearing_detail(appearing_detail_body: wiseword_schema.WisewordBase, db: AsyncSession = Depends(get_db)):
    appearing_detail = await wiseword_crud.get_appearing_detail_by_name(db, appearing_detail_body.appearing_detail)
    if appearing_detail is None:
        raise HTTPException(status_code=404, detail="appearing_detail not found")
    return await wiseword_crud.delete_appearing_detail(db, original=appearing_detail)
