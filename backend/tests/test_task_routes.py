import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from unittest.mock import patch
from src.models.task import Task


def test_create_task(client, session):
    """Test creating a task via API."""
    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123"}):
        response = client.post(
            "/tasks/",
            json={
                "title": "Test Task",
                "description": "This is a test task",
                "completed": False
            },
            headers={"Authorization": "Bearer fake-token"}
        )

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Task"
        assert data["description"] == "This is a test task"
        assert data["completed"] is False
        assert data["user_id"] == "user123"


def test_list_tasks(client, session):
    """Test listing tasks via API."""
    # Create some tasks in the database
    from src.models.task import Task as TaskModel
    from datetime import datetime

    task1 = TaskModel(
        title="Task 1",
        description="First task",
        completed=False,
        user_id="user123",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    task2 = TaskModel(
        title="Task 2",
        description="Second task",
        completed=True,
        user_id="user123",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task1)
    session.add(task2)
    session.commit()

    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123"}):
        response = client.get("/tasks/", headers={"Authorization": "Bearer fake-token"})

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        titles = {task["title"] for task in data}
        assert titles == {"Task 1", "Task 2"}


def test_get_task_by_id(client, session):
    """Test getting a specific task by ID via API."""
    # Create a task in the database
    from src.models.task import Task as TaskModel
    from datetime import datetime

    task = TaskModel(
        title="Specific Task",
        description="A specific task",
        completed=False,
        user_id="user123",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123"}):
        response = client.get(f"/tasks/{task.id}", headers={"Authorization": "Bearer fake-token"})

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Specific Task"
        assert data["description"] == "A specific task"
        assert data["completed"] is False
        assert data["id"] == task.id


def test_update_task(client, session):
    """Test updating a task via API."""
    # Create a task in the database
    from src.models.task import Task as TaskModel
    from datetime import datetime

    task = TaskModel(
        title="Original Task",
        description="Original description",
        completed=False,
        user_id="user123",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123"}):
        response = client.put(
            f"/tasks/{task.id}",
            json={
                "title": "Updated Task",
                "description": "Updated description",
                "completed": True
            },
            headers={"Authorization": "Bearer fake-token"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Task"
        assert data["description"] == "Updated description"
        assert data["completed"] is True


def test_delete_task(client, session):
    """Test deleting a task via API."""
    # Create a task in the database
    from src.models.task import Task as TaskModel
    from datetime import datetime

    task = TaskModel(
        title="Task to Delete",
        description="Will be deleted",
        completed=False,
        user_id="user123",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123"}):
        response = client.delete(f"/tasks/{task.id}", headers={"Authorization": "Bearer fake-token"})

        assert response.status_code == 204

        # Verify the task was deleted by trying to get it
        response = client.get(f"/tasks/{task.id}", headers={"Authorization": "Bearer fake-token"})
        assert response.status_code == 404


def test_toggle_task_completion(client, session):
    """Test toggling task completion via API."""
    # Create a task in the database
    from src.models.task import Task as TaskModel
    from datetime import datetime

    task = TaskModel(
        title="Toggle Task",
        description="Task to toggle",
        completed=False,
        user_id="user123",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123"}):
        response = client.patch(f"/tasks/{task.id}/toggle", headers={"Authorization": "Bearer fake-token"})

        assert response.status_code == 200
        data = response.json()
        assert data["completed"] is True  # Toggled from False to True

        # Toggle again
        response = client.patch(f"/tasks/{task.id}/toggle", headers={"Authorization": "Bearer fake-token"})
        assert response.status_code == 200
        data = response.json()
        assert data["completed"] is False  # Toggled back to False