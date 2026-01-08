import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.models.task import Task as TaskModel
from datetime import datetime


def test_cross_user_access_prevention(client, session):
    """Test that users cannot access tasks belonging to other users."""
    # Create a task for user1
    task_for_user1 = TaskModel(
        title="User1's Task",
        description="This belongs to user1",
        completed=False,
        user_id="user1",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task_for_user1)
    session.commit()
    session.refresh(task_for_user1)

    # Try to access user1's task as user2
    with patch("src.config.security.verify_token", return_value={"sub": "user2", "type": "access"}):
        response = client.get(f"/tasks/{task_for_user1.id}", headers={"Authorization": "Bearer token-for-user2"})

        # Should return 404 (not found) instead of 403 (forbidden) for security reasons
        # (don't reveal that the task exists for another user)
        assert response.status_code == 404


def test_cross_user_update_prevention(client, session):
    """Test that users cannot update tasks belonging to other users."""
    # Create a task for user1
    task_for_user1 = TaskModel(
        title="User1's Task",
        description="This belongs to user1",
        completed=False,
        user_id="user1",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task_for_user1)
    session.commit()
    session.refresh(task_for_user1)

    # Try to update user1's task as user2
    with patch("src.config.security.verify_token", return_value={"sub": "user2", "type": "access"}):
        response = client.put(
            f"/tasks/{task_for_user1.id}",
            json={"title": "Hacked task"},
            headers={"Authorization": "Bearer token-for-user2"}
        )

        # Should return 404 (not found) instead of 403 (forbidden) for security reasons
        assert response.status_code == 404


def test_cross_user_delete_prevention(client, session):
    """Test that users cannot delete tasks belonging to other users."""
    # Create a task for user1
    task_for_user1 = TaskModel(
        title="User1's Task",
        description="This belongs to user1",
        completed=False,
        user_id="user1",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task_for_user1)
    session.commit()
    session.refresh(task_for_user1)

    # Try to delete user1's task as user2
    with patch("src.config.security.verify_token", return_value={"sub": "user2", "type": "access"}):
        response = client.delete(f"/tasks/{task_for_user1.id}", headers={"Authorization": "Bearer token-for-user2"})

        # Should return 404 (not found) instead of 403 (forbidden) for security reasons
        assert response.status_code == 404


def test_cross_user_toggle_prevention(client, session):
    """Test that users cannot toggle completion status of tasks belonging to other users."""
    # Create a task for user1
    task_for_user1 = TaskModel(
        title="User1's Task",
        description="This belongs to user1",
        completed=False,
        user_id="user1",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task_for_user1)
    session.commit()
    session.refresh(task_for_user1)

    # Try to toggle user1's task as user2
    with patch("src.config.security.verify_token", return_value={"sub": "user2", "type": "access"}):
        response = client.patch(f"/tasks/{task_for_user1.id}/toggle", headers={"Authorization": "Bearer token-for-user2"})

        # Should return 404 (not found) instead of 403 (forbidden) for security reasons
        assert response.status_code == 404


def test_user_can_access_own_tasks(client, session):
    """Test that users can access their own tasks."""
    # Create a task for user1
    task_for_user1 = TaskModel(
        title="User1's Task",
        description="This belongs to user1",
        completed=False,
        user_id="user1",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(task_for_user1)
    session.commit()
    session.refresh(task_for_user1)

    # User1 should be able to access their own task
    with patch("src.config.security.verify_token", return_value={"sub": "user1", "type": "access"}):
        response = client.get(f"/tasks/{task_for_user1.id}", headers={"Authorization": "Bearer token-for-user1"})

        # Should return 200 (success)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "User1's Task"