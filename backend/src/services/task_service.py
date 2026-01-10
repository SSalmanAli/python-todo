from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.models.task import Task, TaskUpdate
from src.schemas.task import TaskCreateRequest, TaskUpdateRequest


class TaskService:
    """Service layer for task operations, extracted from CLI implementation."""

    @staticmethod
    def create_task(*, session: Session, task_data: TaskCreateRequest, user_id: str) -> Task:
        """Create a new task for the given user."""
        try:
            task = Task(
                title=task_data.title,
                description=task_data.description,
                completed=task_data.completed,
                user_id=user_id
            )
            session.add(task)
            session.commit()
            session.refresh(task)
            return task
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error creating task due to data integrity issue"
            )
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred while creating task"
            )

    @staticmethod
    def get_task_by_id(*, session: Session, task_id: int, user_id: str) -> Task:
        """Retrieve a specific task by ID for the given user."""
        try:
            statement = select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
            task = session.exec(statement).first()
            if not task:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Task not found or access denied"
                )
            return task
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred while retrieving task"
            )

    @staticmethod
    def get_tasks_by_user(*, session: Session, user_id: str) -> List[Task]:
        """Retrieve all tasks for the given user."""
        try:
            statement = select(Task).where(Task.user_id == user_id)
            tasks = session.exec(statement).all()
            return tasks
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred while retrieving tasks"
            )

    @staticmethod
    def update_task(*, session: Session, task_id: int, task_update: TaskUpdateRequest, user_id: str) -> Task:
        """Update an existing task for the given user."""
        try:
            task = TaskService.get_task_by_id(session=session, task_id=task_id, user_id=user_id)

            # Prepare update data
            update_data = task_update.model_dump(exclude_unset=True)

            # Update task fields
            for field, value in update_data.items():
                setattr(task, field, value)

            # Update the timestamp
            task.updated_at = datetime.utcnow()

            session.add(task)
            session.commit()
            session.refresh(task)
            return task
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error updating task due to data integrity issue"
            )
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred while updating task"
            )

    @staticmethod
    def delete_task(*, session: Session, task_id: int, user_id: str) -> bool:
        """Delete a task for the given user."""
        try:
            task = TaskService.get_task_by_id(session=session, task_id=task_id, user_id=user_id)
            session.delete(task)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred while deleting task"
            )

    @staticmethod
    def toggle_task_completion(*, session: Session, task_id: int, user_id: str) -> Task:
        """Toggle the completion status of a task for the given user."""
        try:
            task = TaskService.get_task_by_id(session=session, task_id=task_id, user_id=user_id)
            task.completed = not task.completed
            task.updated_at = datetime.utcnow()
            session.add(task)
            session.commit()
            session.refresh(task)
            return task
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error toggling task completion due to data integrity issue"
            )
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred while toggling task completion"
            )