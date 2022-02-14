from pydantic import BaseModel
from datetime import datetime
from typing import List


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class Comment(BaseModel):
    text: str
    username: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    created_at: datetime
    user: User
    comments: List[Comment]

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    text: str
    post_id: int
