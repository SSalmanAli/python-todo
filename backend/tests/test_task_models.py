import pytest
from src.models.task import Task


def test_task_creation():
    """Test creating a task model instance."""
    task = Task(
        title="Test Task",
        description="This is a test task",
        completed=False,
        user_id="user123"
    )

    assert task.title == "Test Task"
    assert task.description == "This is a test task"
    assert task.completed is False
    assert task.user_id == "user123"
    assert task.id is None  # ID will be set by the database


def test_task_default_values():
    """Test that task model has correct default values."""
    task = Task(
        title="Test Task",
        user_id="user123"
    )

    assert task.title == "Test Task"
    assert task.completed is False  # Default value
    assert task.user_id == "user123"


def test_task_required_fields():
    """Test that required fields are enforced."""
    # Title is required
    with pytest.raises(ValueError):
        Task(
            title="",  # Empty title should fail
            user_id="user123"
        )

    # User ID is required
    with pytest.raises(ValueError):
        Task(
            title="Test Task",
            user_id=""  # Empty user_id should fail
        )