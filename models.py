from sqlalchemy import ForeignKey, Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from database import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    state = Column(Boolean)
    group_id = Column(Integer, ForeignKey("groups.id"))

    owner = relationship("Group", back_populates="tasks")


