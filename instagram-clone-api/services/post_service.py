from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from typing import List
from schemas.post_schema import PostBase, PostDisplay
from schemas.user_schema import UserAuth
from models.post_model import Post


def create_post(db: Session, current_user: UserAuth, request: PostBase) -> PostDisplay:
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=current_user.id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session) -> List[PostDisplay]:
    return db.query(Post).all()


def delete_post(db: Session, current_user: UserAuth, id: int):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only post creator can delete post",
        )

    db.delete(post)
    db.commit()
    return "ok"
