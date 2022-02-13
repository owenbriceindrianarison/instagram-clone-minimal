from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from schemas.user_schema import UserDisplay, UserBase
from utils.util import get_db
from services.user_service import create_user, login_user

# from utils.oauth2 import create_access_token
from utils import oauth2

router = APIRouter(tags=["authentication"])


@router.post("/register", response_model=UserDisplay)
def register(request: UserBase, db: Session = Depends(get_db)):
    return create_user(db, request)


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    return login_user(db, request)
