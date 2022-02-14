from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class AccessToken(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    username: str


class UserAuth(BaseModel):
    id: int
    username: str
    email: str
