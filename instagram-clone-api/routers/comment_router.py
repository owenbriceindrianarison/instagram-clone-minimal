from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List
from schemas.post_schema import CommentBase, Comment
from schemas.user_schema import UserAuth
from utils.util import get_db
from utils import oauth2
from services import comment_service


router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("/{post_id}", response_model=List[Comment])
def get_posts(post_id: int, db: Session = Depends(get_db)):
    return comment_service.get_all_comments(db, post_id)


@router.post("/")
def create(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(oauth2.get_current_user),
):
    return comment_service.create_comment(db, current_user, request)
