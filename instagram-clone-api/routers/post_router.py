from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from schemas.post_schema import PostBase, PostDisplay
from utils.db_util import get_db
from services.post_service import create_post

router = APIRouter(prefix="/posts", tags=["posts"])

image_url_types = ["absolute", "relative"]


@router.post("/", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.",
        )
    return create_post(db, request)
