from pydantic import BaseModel
from datetime import datetime

from core.models.user import UserStatus


class UserBase(BaseModel):
    username: str
    password: str
    name: str
    last_name: str
    speciality: str
    tg_id: int
    prodoctor_url: str
    is_active: UserStatus
    is_banned: bool
    files: str
    created_at: datetime
    updated_at: datetime





class UserCreate(UserBase):
    pass

class UserRead(UserBase): 
    id: int
