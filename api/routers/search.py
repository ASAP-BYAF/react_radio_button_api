from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.search as search_schema
import api.cruds.search as search_crud
from api.db import get_db

router = APIRouter()


@router.get("/search", response_model=list[search_schema.SearchBase])
async def list_searchs(db: AsyncSession = Depends(get_db)):
    return await search_crud.get_all(db)


@router.post("/search_filtered_by_task", response_model=list[search_schema.SearchBase])
async def list_searchs_filtered_by_task(search_body: search_schema.SearchByTask, db: AsyncSession = Depends(get_db)):
    # print(search_body.TaskList)
    # return await search_crud.get_all(db)
    return await search_crud.get_filtered_by_task(db)
    # print(tmp)
    # return
