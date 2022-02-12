from sqlalchemy.orm.session import Session
from schemas.user_schema import UserBase, User as UserSchema
from models.user_model import User
from utils.hashing import Hash


def create_user(db: Session, request: UserBase) -> UserSchema:
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
