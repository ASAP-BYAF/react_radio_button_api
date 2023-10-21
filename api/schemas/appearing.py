from pydantic import BaseModel


class AppearingBase(BaseModel):
    file_id: int
    task_id: int
    appearing_detail_id: int


class AppearingDelete(BaseModel):
    file_id: int
    task_id: int


class AppearingCreate(AppearingBase):
    pass


class AppearingCreateResponse(AppearingCreate):
    pass

    class Config:
        orm_mode = True
