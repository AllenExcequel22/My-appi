from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from services.db import get_db
from models import schemas
from controllers import crud

router = APIRouter(prefix="/items",tags=["items"])

@router.get("/",response_model=List[schemas.ItemOut],tags=["items"])
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)