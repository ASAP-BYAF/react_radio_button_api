from pydantic import BaseModel


class FileBase(BaseModel):
    vol_num: int
    file_num: int


class FileSerachByName(BaseModel):
    file_name: str


class FileCreate(FileBase):
    file_name: str


class FileCreateResponse(FileCreate):
    id: int

    class Config:
        orm_mode = True