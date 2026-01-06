"""
Todo service for managing tasks in memory.
"""
from typing import Dict, List, Optional
from src.models.task import Task


class TodoService:
    """
    Service class for managing todo tasks in memory.
    """
    def __init__(self):
        """Initialize the service with an empty task collection."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with the given title and optional description.

        Args:
            title: The task title
            description: Optional task description

        Returns:
            The created Task object with assigned ID
        """
        task_id = self._next_id
        self._next_id += 1
        task = Task(id=task_id, title=title, description=description, completed=False)
        self._tasks[task_id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List of all Task objects
        """
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if it didn't exist
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_task(self, task_id: int, completed: bool) -> Optional[Task]:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: The ID of the task to update
            completed: True to mark as complete, False to mark as incomplete

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        task.completed = completed
        return task