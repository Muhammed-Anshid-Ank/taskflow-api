from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=schemas.AdminResponse)
def signup(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db, admin.username, admin.password)

@router.post("/apikey", response_model=schemas.APIKeyResponse)
def generate_api_key(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    auth = crud.authenticate_admin(db, admin.username, admin.password)
    if not auth:
        raise HTTPException(status_code=401, detail="Invalid admin credentials")
    return crud.create_api_key(db)
