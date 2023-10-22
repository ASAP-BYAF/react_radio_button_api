from pydantic import BaseModel


class SearchBase(BaseModel):
    vol_num: int
    file_num: int
    title: str
    appearing_detail: str

    class Config:
        orm_mode = True
