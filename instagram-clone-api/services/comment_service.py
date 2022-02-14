from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from models.comment_model import Comment
from schemas.post_schema import CommentBase
from schemas.user_schema import UserAuth


def create_comment(db: Session, current_user: UserAuth, request: CommentBase):
    new_comment = Comment(
        text=request.text, username=current_user.username, post_id=request.post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all_comments(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()
