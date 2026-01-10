from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreateRequest(BaseModel):
    """Schema for creating a new task."""
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskUpdateRequest(BaseModel):
    """Schema for updating an existing task."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    """Schema for task response."""
    id: int
    user_id: str
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True