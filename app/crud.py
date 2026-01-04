from sqlalchemy.orm import Session
from app import models
import secrets

# -------- ADMIN --------

def create_admin(db: Session, username: str, password: str):
    admin = models.Admin(username=username, password=password)
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def authenticate_admin(db: Session, username: str, password: str):
    return db.query(models.Admin).filter(
        models.Admin.username == username,
        models.Admin.password == password
    ).first()

# -------- API KEY --------

def create_api_key(db: Session):
    key = secrets.token_hex(32)
    api_key = models.APIKey(key=key)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)
    return api_key

def validate_api_key(db: Session, key: str):
    return db.query(models.APIKey).filter(
        models.APIKey.key == key,
        models.APIKey.is_active == True
    ).first()

# -------- USERS --------

def create_user(db: Session, name: str, email: str):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    return db.query(models.User).all()

# -------- TASKS --------

def create_task(db: Session, title: str, description: str, user_id: int):
    task = models.Task(title=title, description=description, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    return db.query(models.Task).all()

def update_task(db: Session, task_id: int, status: str):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

