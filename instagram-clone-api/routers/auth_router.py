from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schemas.user_schema import UserDisplay, UserBase
from utils.util import get_db
from services.user_service import create_user

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=UserDisplay)
def register(request: UserBase, db: Session = Depends(get_db)):
    return create_user(db, request)
