from typing import Annotated

from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    equipment_id: str
    student_id: int
    description: str
    priority: int
    status: int

