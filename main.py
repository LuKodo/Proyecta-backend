from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import schemas, models

from database import engine,SessionLocal
import CRUD.projects as projects, CRUD.tasks as tasks
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
    allow_origins=["http://localhost:5173", "https://brilliant-rabanadas-105dfa.netlify.app", "https://42e6-190-68-152-214.ngrok-free.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/projects", tags=["Projects"])
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = projects.create(db=db, project=project)
    return db_project

@app.get("/project/{project_id}", tags=["Projects"])
def get_one(project_id: int, db: Session = Depends(get_db)):
    db_project = projects.get_one(db=db, project_id=project_id)
    return db_project

@app.get("/projects", tags=["Projects"])
def get_all(db: Session = Depends(get_db)):
    db_projects = projects.get_all(db=db)
    return db_projects

@app.patch("/projects/{project_id}", tags=["Projects"])
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = projects.refresh(db=db, project_id=project_id, project=project)
    return db_project
    
@app.delete("/project/{project_id}", tags=["Projects"])
def delete_project(project_id: int, db: Session = Depends(get_db)):
    return projects.delete(db=db, project_id=project_id)

@app.get("/tasks/{project_id}", tags=["Tasks"])
def get_all_task(project_id: int, db: Session = Depends(get_db)):
    db_tasks = tasks.get_all(db=db, project_id=project_id)
    return db_tasks

@app.post("/task", tags=["Tasks"])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = tasks.create(db=db, task=task)
    return db_task

@app.get("/task/{task_id}", tags=["Tasks"])
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    db_task = tasks.get_one(db=db, task_id=task_id)
    return db_task

@app.patch("/task/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: schemas.Task, db: Session = Depends(get_db)):
    db_task = tasks.refresh(db=db, task_id=task_id, task=task)
    return db_task

@app.delete("/task/{task_id}", tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return tasks.delete(db=db, task_id=task_id)
