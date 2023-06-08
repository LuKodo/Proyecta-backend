from typing import Union
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Union[str, None] = None
    state: bool
    group_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    tasks: list[Task] = []

    class Config:
        orm_mode = True