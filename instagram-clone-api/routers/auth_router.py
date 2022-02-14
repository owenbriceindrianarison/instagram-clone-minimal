from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from schemas.user_schema import AccessToken, UserBase
from utils.util import get_db
from services import user_service

# from utils.oauth2 import create_access_token
from utils import oauth2

router = APIRouter(tags=["authentication"])


@router.post("/register", response_model=AccessToken)
def register(request: UserBase, db: Session = Depends(get_db)):
    return user_service.create_user(db, request)


@router.post("/login", response_model=AccessToken)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    return user_service.login_user(db, request)
