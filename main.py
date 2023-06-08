from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import schemas, models

from database import engine,SessionLocal
import groupsCRUD, tasksCRUD
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/groups", tags=["Groups"])
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = groupsCRUD.create(db=db, group=group)
    return db_group

@app.get("/group/{group_id}", tags=["Groups"])
def get_one(group_id: int, db: Session = Depends(get_db)):
    db_group = groupsCRUD.get_one(db=db, group_id=group_id)
    return db_group

@app.get("/groups", tags=["Groups"])
def get_all(db: Session = Depends(get_db)):
    db_groups = groupsCRUD.get_all(db=db)
    return db_groups

@app.patch("/groups/{group_id}", tags=["Groups"])
def update_group(group_id: int, group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = groupsCRUD.refresh(db=db, group_id=group_id, group=group)
    return db_group
    
@app.delete("/group/{group_id}", tags=["Groups"])
def delete_group(group_id: int, db: Session = Depends(get_db)):
    return groupsCRUD.delete(db=db, group_id=group_id)

@app.get("/tasks/{group_id}", tags=["Tasks"])
def get_all_task(group_id: int, db: Session = Depends(get_db)):
    db_tasks = tasksCRUD.get_all(db=db, group_id=group_id)
    return db_tasks

@app.post("/task", tags=["Tasks"])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = tasksCRUD.create(db=db, task=task)
    return db_task

@app.get("/task/{task_id}", tags=["Tasks"])
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    db_task = tasksCRUD.get_one(db=db, task_id=task_id)
    return db_task

@app.patch("/task/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: schemas.Task, db: Session = Depends(get_db)):
    db_task = tasksCRUD.refresh(db=db, task_id=task_id, task=task)
    return db_task

@app.delete("/task/{task_id}", tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return tasksCRUD.delete(db=db, task_id=task_id)
