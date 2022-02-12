from sqlalchemy.orm.session import Session
from schemas.post_schema import PostBase, PostDisplay
from models.post_model import Post


def create_post(db: Session, request: PostBase) -> PostDisplay:
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
