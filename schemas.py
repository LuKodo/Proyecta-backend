from typing import Union
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Union[str, None] = None
    state: bool
    project_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    tasks: list[Task] = []

    class Config:
        orm_mode = True