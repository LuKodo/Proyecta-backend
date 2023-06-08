from fastapi import HTTPException, status
from sqlalchemy import update
from sqlalchemy.orm import Session
import models, schemas

# Create
def create(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        state=task.state,
        group_id=task.group_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Read One
def get_one(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Read All
def get_all(db: Session, group_id: int):
    return db.query(models.Task).filter(models.Task.group_id == group_id).all()

# Update
def refresh(db: Session, task_id: int,  task: schemas.Task):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    db_task.state = task.state
    db_task.title = task.title   
    db_task.description = task.description
    db.commit()
    
    return get_one(db=db, task_id=task_id)

# Delete
def delete(db: Session, task_id: int):
    db_task = get_one(db=db, task_id=task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        db.close()
        return "Task deleted"
    else:
        raise HTTPException(status_code=404, detail=f"group with id {group_id} not found")
