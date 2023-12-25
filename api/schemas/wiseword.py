from pydantic import BaseModel


class WisewordBase(BaseModel):
    phrase: str
    task_id: int


class WisewordCreate(WisewordBase):
    file_id: int


class WisewordCreateResponse(WisewordCreate):
    id: int

    class Config:
        orm_mode = True

class WisewordGetResponse(BaseModel):
    id: int
    phrase: str
    title: str
    vol_num: int
    file_num: int

    class Config:
        orm_mode = True
