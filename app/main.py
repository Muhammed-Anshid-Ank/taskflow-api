from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import admin, users, tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")

app.include_router(admin.router)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "TaskFlow API running"}
