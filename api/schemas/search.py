from pydantic import BaseModel, Field


class SearchBase(BaseModel):
    file_id: int
    task_id: int
    appearing_detail_id: int

    class Config:
        orm_mode = True
