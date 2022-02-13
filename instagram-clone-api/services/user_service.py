from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from schemas.user_schema import UserBase, UserDisplay
from models.user_model import User
from utils.hashing import Hash
from utils import oauth2


def create_user(db: Session, request: UserBase) -> UserDisplay:
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return UserSchema.from_orm(new_user)
    return new_user


def login_user(db: Session, request: OAuth2PasswordRequestForm):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    access_token = oauth2.create_access_token(data={"username": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
    }
