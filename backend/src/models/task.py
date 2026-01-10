from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class TaskBase(SQLModel):
    """Base class for Task model with common fields."""
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str = Field(max_length=255, index=True)


class Task(TaskBase, table=True):
    """Task model representing a user's todo item."""
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TaskUpdate(TaskBase):
    """Schema for updating a task."""
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = Field(default=None)
    user_id: Optional[str] = Field(default=None, max_length=255)