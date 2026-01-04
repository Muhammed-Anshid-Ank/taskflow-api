from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------- ADMIN --------

class AdminCreate(BaseModel):
    username: str
    password: str

class AdminResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


# -------- API KEY --------

class APIKeyResponse(BaseModel):
    key: str
    created_at: datetime

    class Config:
        from_attributes = True


# -------- USER --------

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


# -------- TASK --------

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int

class TaskUpdate(BaseModel):
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
