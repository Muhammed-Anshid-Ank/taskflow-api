from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from app.security import get_api_key

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    user = crud.get_user_by_id(db, task.user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {task.user_id} does not exist"
        )

    return crud.create_task(db, task.title, task.description, task.user_id)


@router.get("/", response_model=list[schemas.TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    return crud.get_tasks(db)

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    updated = crud.update_task(db, task_id, task.status)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated
