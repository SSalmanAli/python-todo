import pytest
from sqlmodel import Session, select
from src.models.task import Task
from src.config.database import engine


def test_database_connection():
    """Test that we can connect to the database."""
    # This test verifies that the database engine is configured correctly
    # It doesn't require the client fixture since we're testing at a lower level

    # Try to create a session and execute a simple query
    with Session(engine) as session:
        # Execute a simple query to test the connection
        result = session.exec(select(1))
        assert result.one() == 1


def test_database_session_fixture(session):
    """Test that the session fixture works correctly."""
    # Create a task directly through the session
    task = Task(
        title="Database Test Task",
        description="Task created through database session",
        completed=False,
        user_id="testuser"
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    assert task.id is not None
    assert task.title == "Database Test Task"
    assert task.user_id == "testuser"


def test_task_creation_and_retrieval(session):
    """Test creating and retrieving a task through the database."""
    # Create a task
    original_task = Task(
        title="Test Task",
        description="This is a test task",
        completed=False,
        user_id="testuser"
    )

    session.add(original_task)
    session.commit()
    session.refresh(original_task)

    # Verify the task was created with an ID
    assert original_task.id is not None
    assert original_task.title == "Test Task"

    # Retrieve the task from the database
    retrieved_task = session.get(Task, original_task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == original_task.id
    assert retrieved_task.title == original_task.title
    assert retrieved_task.description == original_task.description
    assert retrieved_task.completed == original_task.completed
    assert retrieved_task.user_id == original_task.user_id


def test_multiple_tasks_for_user(session):
    """Test creating multiple tasks for the same user."""
    user_id = "testuser"

    # Create multiple tasks for the same user
    task1 = Task(title="Task 1", description="First task", completed=False, user_id=user_id)
    task2 = Task(title="Task 2", description="Second task", completed=True, user_id=user_id)
    task3 = Task(title="Task 3", description="Third task", completed=False, user_id=user_id)

    session.add(task1)
    session.add(task2)
    session.add(task3)
    session.commit()

    # Verify all tasks were created with IDs
    assert task1.id is not None
    assert task2.id is not None
    assert task3.id is not None

    # Verify they all have the same user_id
    assert task1.user_id == user_id
    assert task2.user_id == user_id
    assert task3.user_id == user_id