from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.search as search_schema
import api.cruds.search as search_crud
from api.db import get_db
from api.util.grouped_data import grouped_data_func

router = APIRouter()


@router.get("/search", response_model= dict[int, dict[int, list[dict[str, str]]]])
async def list_searchs(db: AsyncSession = Depends(get_db)):
    data = await search_crud.get_all(db)
    print(grouped_data_func(data))
    return grouped_data_func(data)


# @router.post("/search_filtered_by_task", response_model=list[search_schema.SearchBase])
@router.post("/search_filtered_by_task", response_model= dict[int, dict[int, list[dict[str, str]]]])
async def list_searchs_filtered_by_task(search_body: search_schema.SearchByTask, db: AsyncSession = Depends(get_db)):
    data = await search_crud.get_all(db)
    return grouped_data_func(data)
