from pydantic import BaseMode
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class User(UserBase):
    id: int
    date_created: datetime

    class Config:
        orm_mode = True
