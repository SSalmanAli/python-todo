"""
End-to-end integration tests for the FastAPI Todo Backend Service.
Tests the complete workflow from API request to database persistence.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app
from sqlmodel import select
from src.models.task import Task
from src.config.database import engine
from src.config.security import create_access_token


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    with TestClient(app) as client:
        yield client


def test_complete_workflow_integration(client):
    """Test the complete workflow: create, list, update, toggle, delete."""
    # Create a valid JWT token for testing
    user_id = "integration_test_user"
    token_data = {"sub": user_id}
    token = create_access_token(data=token_data)

    headers = {"Authorization": f"Bearer {token}"}

    # Step 1: Create a task
    create_response = client.post(
        "/tasks/",
        json={
            "title": "Integration Test Task",
            "description": "This is a task for integration testing",
            "completed": False
        },
        headers=headers
    )

    assert create_response.status_code == 201
    created_task = create_response.json()
    assert created_task["title"] == "Integration Test Task"
    assert created_task["description"] == "This is a task for integration testing"
    assert created_task["completed"] is False
    assert created_task["user_id"] == user_id

    task_id = created_task["id"]

    # Step 2: Get the task by ID
    get_response = client.get(f"/tasks/{task_id}", headers=headers)
    assert get_response.status_code == 200

    retrieved_task = get_response.json()
    assert retrieved_task["id"] == task_id
    assert retrieved_task["title"] == "Integration Test Task"

    # Step 3: List all tasks for the user
    list_response = client.get("/tasks/", headers=headers)
    assert list_response.status_code == 200

    tasks_list = list_response.json()
    assert len(tasks_list) == 1
    assert tasks_list[0]["id"] == task_id

    # Step 4: Update the task
    update_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Integration Test Task",
            "description": "Updated description for integration testing",
            "completed": True
        },
        headers=headers
    )

    assert update_response.status_code == 200
    updated_task = update_response.json()
    assert updated_task["title"] == "Updated Integration Test Task"
    assert updated_task["completed"] is True

    # Step 5: Toggle the task completion status
    toggle_response = client.patch(f"/tasks/{task_id}/toggle", headers=headers)
    assert toggle_response.status_code == 200

    toggled_task = toggle_response.json()
    assert toggled_task["completed"] is False  # Should be False after toggle

    # Step 6: Verify the task exists in the database directly
    with engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text("SELECT * FROM task WHERE id = :id"), {"id": task_id})
        db_task = result.fetchone()
        assert db_task is not None

    # Step 7: Delete the task
    delete_response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert delete_response.status_code == 204

    # Step 8: Verify the task is gone
    not_found_response = client.get(f"/tasks/{task_id}", headers=headers)
    assert not_found_response.status_code == 404


def test_user_isolation_integration(client):
    """Test that users can only access their own tasks."""
    # Create tokens for two different users
    user1_id = "user1_integration"
    user2_id = "user2_integration"

    token1 = create_access_token(data={"sub": user1_id})
    token2 = create_access_token(data={"sub": user2_id})

    user1_headers = {"Authorization": f"Bearer {token1}"}
    user2_headers = {"Authorization": f"Bearer {token2}"}

    # User 1 creates a task
    create_response = client.post(
        "/tasks/",
        json={
            "title": "User1's Task",
            "description": "Task created by user1",
            "completed": False
        },
        headers=user1_headers
    )

    assert create_response.status_code == 201
    user1_task = create_response.json()
    user1_task_id = user1_task["id"]

    # User 2 should not be able to access User 1's task
    forbidden_response = client.get(f"/tasks/{user1_task_id}", headers=user2_headers)
    assert forbidden_response.status_code == 404  # Should return 404 instead of 403 for security

    # User 2 creates their own task
    create_response2 = client.post(
        "/tasks/",
        json={
            "title": "User2's Task",
            "description": "Task created by user2",
            "completed": False
        },
        headers=user2_headers
    )

    assert create_response2.status_code == 201
    user2_task = create_response2.json()
    user2_task_id = user2_task["id"]

    # Verify user isolation: each user sees only their own tasks
    user1_tasks_response = client.get("/tasks/", headers=user1_headers)
    assert user1_tasks_response.status_code == 200
    user1_tasks = user1_tasks_response.json()
    assert len(user1_tasks) == 1
    assert user1_tasks[0]["id"] == user1_task_id

    user2_tasks_response = client.get("/tasks/", headers=user2_headers)
    assert user2_tasks_response.status_code == 200
    user2_tasks = user2_tasks_response.json()
    assert len(user2_tasks) == 1
    assert user2_tasks[0]["id"] == user2_task_id


def test_error_scenarios_integration(client):
    """Test various error scenarios."""
    # Create a valid token for testing
    user_id = "error_test_user"
    token = create_access_token(data={"sub": user_id})
    headers = {"Authorization": f"Bearer {token}"}

    # Test creating task without required fields
    bad_request_response = client.post(
        "/tasks/",
        json={"description": "Task without title"},  # Missing required title
        headers=headers
    )
    assert bad_request_response.status_code == 422  # Validation error

    # Test accessing non-existent task
    not_found_response = client.get("/tasks/999999", headers=headers)
    assert not_found_response.status_code == 404

    # Test accessing API without token
    unauthorized_response = client.get("/tasks/")
    assert unauthorized_response.status_code in [403, 422, 401]  # Should be unauthorized