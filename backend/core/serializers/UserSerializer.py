from datetime import datetime

from pydantic import BaseModel


class UserOut(BaseModel):
    id: str
    name: str
    email: str
    avatar: int
    create_at: datetime


class UserIn(BaseModel):
    name: str
    email: str
    avatar: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str
