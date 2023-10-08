from pydantic import BaseModel


class AppearingDetailBase(BaseModel):
    appearing_detail: str


class AppearingDetailCreate(AppearingDetailBase):
    pass


class AppearingDetailCreateResponse(AppearingDetailCreate):
    id: int

    class Config:
        orm_mode = True
