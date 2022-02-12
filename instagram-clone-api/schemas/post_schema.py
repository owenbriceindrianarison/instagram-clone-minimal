from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    created_at: datetime
    user: User

    class Config:
        orm_mode = True
