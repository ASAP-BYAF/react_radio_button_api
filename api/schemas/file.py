from pydantic import BaseModel, Field


class FileBase(BaseModel):
    vol_num: int
    file_num: int

class FileCreate(FileBase):
    file_name: str

class FileCreateResponse(FileCreate):
    id: int

    class Config:
        orm_mode = True