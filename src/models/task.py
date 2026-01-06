"""
Task data model for the Todo application.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task with ID, title, description, and completion status.
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        """Validate task attributes after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")