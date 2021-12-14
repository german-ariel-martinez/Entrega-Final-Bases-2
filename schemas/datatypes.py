from typing import Optional
from pydantic import BaseModel
from datetime import date, time

class CreateUser(BaseModel):
    user_id: Optional[int]
    username: str
    sex: str
    age: str
    description: str
    instagram: Optional[str]
    facebook: Optional[str]
    twitter: Optional[str]
    linkedin: Optional[str]
    email: str
    password: str

class User(BaseModel):
    username: str
    sex: str
    age: str
    description: str
    instagram: str
    facebook: str
    twitter: str
    linkedin: str

class CreateEvent(BaseModel):
    event_id: Optional[int]
    title: str
    date: date
    hour: time
    description: str
    location: str
    host: int

class Event(BaseModel):
    event_id: int
    title: str
    date: date
    hour: time
    description: str
    location: str
    host: int

class UserID(BaseModel):
    user_id: int

# Tipos de estados:
#   0 -> no asiste
#   1 -> asiste
#   2 -> no sabe (no se si agregarlo)
class Assists(BaseModel):
    user_id: int
    event_id: int
    status: int

class Response(BaseModel):
    status: int
    detail: dict

class Login(BaseModel):
    email: str
    password: str
    