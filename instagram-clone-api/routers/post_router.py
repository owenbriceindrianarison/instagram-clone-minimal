from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List
from schemas.post_schema import PostBase, PostDisplay
from schemas.user_schema import UserAuth
from utils.util import get_db, upload_file
from utils import oauth2
from services import post_service


router = APIRouter(prefix="/posts", tags=["posts"])

image_url_types = ["absolute", "relative"]


@router.post("/", response_model=PostDisplay)
def create(
    request: PostBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(oauth2.get_current_user),
):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.",
        )
    return post_service.create_post(db, current_user, request)


@router.get("/", response_model=List[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return post_service.get_all_posts(db)


@router.delete("/{id}")
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(oauth2.get_current_user),
):
    return post_service.delete_post(db, current_user, id)


@router.post("/image")
def upload_image(
    image: UploadFile = File(...),
    current_user: UserAuth = Depends(oauth2.get_current_user),
):
    return upload_file(image)
