from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False

class TodoUpdate(TodoCreate):
    completed: bool

class TodoInDB(TodoCreate):
    id: int

    class Config:
        orm_mode = True
