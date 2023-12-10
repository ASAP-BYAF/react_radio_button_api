from pydantic import BaseModel


class WisewordBase(BaseModel):
    phrase: str


class WisewordCreate(WisewordBase):
    file_id: int


class WisewordCreateResponse(WisewordCreate):
    id: int

    class Config:
        orm_mode = True
