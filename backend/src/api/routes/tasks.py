from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from src.config.database import get_session
from src.config.security import get_current_user
from src.services.task_service import TaskService
from src.schemas.task import TaskCreateRequest, TaskUpdateRequest, TaskResponse

router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
async def list_tasks(
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """List all tasks for the current user."""
    tasks = TaskService.get_tasks_by_user(session=session, user_id=current_user)
    return tasks


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreateRequest,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new task for the current user."""
    task = TaskService.create_task(
        session=session,
        task_data=task_data,
        user_id=current_user
    )
    return task


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get a specific task by ID."""
    task = TaskService.get_task_by_id(
        session=session,
        task_id=task_id,
        user_id=current_user
    )
    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_update: TaskUpdateRequest,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update a specific task by ID."""
    task = TaskService.update_task(
        session=session,
        task_id=task_id,
        task_update=task_update,
        user_id=current_user
    )
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Delete a specific task by ID."""
    TaskService.delete_task(
        session=session,
        task_id=task_id,
        user_id=current_user
    )
    return


@router.patch("/{task_id}/toggle", response_model=TaskResponse)
async def toggle_task_completion(
    task_id: int,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a task."""
    task = TaskService.toggle_task_completion(
        session=session,
        task_id=task_id,
        user_id=current_user
    )
    return task