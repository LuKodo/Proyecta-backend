from fastapi import HTTPException, status
from sqlalchemy import update
from sqlalchemy.orm import Session
import models, schemas
import CRUD.tasks as tasks

# Create
def create(db: Session, project: schemas.ProjectCreate):
    exists = db.query(models.Project).filter(models.Project.name == project.name).first()
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Existe un grupo con este nombre"
        )
    else:
        db_project = models.Project(name=project.name)
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

# Read One
def get_one(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

# Read All
def get_all(db: Session):
    return db.query(models.Project).all()

# Update
def refresh(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    db_project.name = project.name    
    db.commit()
    
    return get_one(db=db, project_id=project_id)

# Delete
def delete(db: Session, project_id):
    db_project = get_one(db=db, project_id=project_id)
    if db_project:
        db_task = tasks.get_all(db=db, project_id=project_id)
        if(db_task):
            raise HTTPException(
                status_code=444,
                detail="El proyecto tiene actividades, eliminelas para poder eliminar el proyecto"
            )
        db.delete(db_project)
        db.commit()
        db.close()
        return "deleted"
    else:
        raise HTTPException(status_code=404, detail=f"project with id {project_id} not found")
