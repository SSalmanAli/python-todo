import pytest
from datetime import datetime
from src.schemas.task import TaskCreateRequest, TaskUpdateRequest, TaskResponse


def test_task_create_request():
    """Test TaskCreateRequest schema."""
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False
    }

    task_create = TaskCreateRequest(**task_data)

    assert task_create.title == "Test Task"
    assert task_create.description == "This is a test task"
    assert task_create.completed is False


def test_task_create_request_required_fields():
    """Test that TaskCreateRequest requires title."""
    # Should work with just title
    task_create = TaskCreateRequest(title="Test Task")
    assert task_create.title == "Test Task"
    assert task_create.completed is False  # Default value

    # Should fail without title
    with pytest.raises(ValueError):
        TaskCreateRequest(title="")  # Empty title should fail


def test_task_update_request():
    """Test TaskUpdateRequest schema."""
    task_update = TaskUpdateRequest(
        title="Updated Title",
        description="Updated description",
        completed=True
    )

    assert task_update.title == "Updated Title"
    assert task_update.description == "Updated description"
    assert task_update.completed is True


def test_task_update_request_optional_fields():
    """Test that all fields in TaskUpdateRequest are optional."""
    # Empty update request should be valid
    task_update = TaskUpdateRequest()
    assert task_update.title is None
    assert task_update.description is None
    assert task_update.completed is None

    # Partial updates should be valid
    task_update = TaskUpdateRequest(title="New Title")
    assert task_update.title == "New Title"
    assert task_update.description is None
    assert task_update.completed is None


def test_task_response():
    """Test TaskResponse schema."""
    task_response_data = {
        "id": 1,
        "user_id": "user123",
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    task_response = TaskResponse(**task_response_data)

    assert task_response.id == 1
    assert task_response.user_id == "user123"
    assert task_response.title == "Test Task"
    assert task_response.description == "This is a test task"
    assert task_response.completed is False