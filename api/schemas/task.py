from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="クリーニングを取りに行く")

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True