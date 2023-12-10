from pydantic import BaseModel


class WisewordBase(BaseModel):
    phrase: str


class WisewordCreate(WisewordBase):
    pass


class WisewordCreateResponse(WisewordCreate):
    id: int

    class Config:
        orm_mode = True
