from src.services.task_service import TaskService
from src.models.task import Task
from src.schemas.task import TaskCreateRequest, TaskUpdateRequest


def test_task_service_create_task(session):
    """Test creating a task using the TaskService."""
    task_data = TaskCreateRequest(
        title="Test Task",
        description="This is a test task",
        completed=False
    )

    user_id = "user123"

    created_task = TaskService.create_task(
        session=session,
        task_data=task_data,
        user_id=user_id
    )

    assert created_task.title == "Test Task"
    assert created_task.description == "This is a test task"
    assert created_task.completed is False
    assert created_task.user_id == user_id
    assert created_task.id is not None


def test_task_service_get_task_by_id(session):
    """Test getting a task by ID using the TaskService."""
    # First create a task
    task_data = TaskCreateRequest(
        title="Test Task",
        description="This is a test task",
        completed=False
    )

    user_id = "user123"

    created_task = TaskService.create_task(
        session=session,
        task_data=task_data,
        user_id=user_id
    )

    # Now get the task by ID
    retrieved_task = TaskService.get_task_by_id(
        session=session,
        task_id=created_task.id,
        user_id=user_id
    )

    assert retrieved_task.id == created_task.id
    assert retrieved_task.title == "Test Task"
    assert retrieved_task.description == "This is a test task"
    assert retrieved_task.completed is False
    assert retrieved_task.user_id == user_id


def test_task_service_get_tasks_by_user(session):
    """Test getting all tasks for a user using the TaskService."""
    user_id = "user123"

    # Create multiple tasks for the user
    task_data1 = TaskCreateRequest(title="Task 1", description="First task")
    task_data2 = TaskCreateRequest(title="Task 2", description="Second task")

    TaskService.create_task(session=session, task_data=task_data1, user_id=user_id)
    TaskService.create_task(session=session, task_data=task_data2, user_id=user_id)

    # Create a task for a different user
    other_user_id = "user456"
    task_data3 = TaskCreateRequest(title="Other Task", description="Task for other user")
    TaskService.create_task(session=session, task_data=task_data3, user_id=other_user_id)

    # Get tasks for the first user
    user_tasks = TaskService.get_tasks_by_user(session=session, user_id=user_id)

    assert len(user_tasks) == 2
    assert all(task.user_id == user_id for task in user_tasks)
    assert set(task.title for task in user_tasks) == {"Task 1", "Task 2"}


def test_task_service_update_task(session):
    """Test updating a task using the TaskService."""
    # Create a task
    task_data = TaskCreateRequest(
        title="Original Task",
        description="Original description",
        completed=False
    )

    user_id = "user123"

    created_task = TaskService.create_task(
        session=session,
        task_data=task_data,
        user_id=user_id
    )

    # Update the task
    update_data = TaskUpdateRequest(
        title="Updated Task",
        description="Updated description",
        completed=True
    )

    updated_task = TaskService.update_task(
        session=session,
        task_id=created_task.id,
        task_update=update_data,
        user_id=user_id
    )

    assert updated_task.id == created_task.id
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated description"
    assert updated_task.completed is True
    assert updated_task.user_id == user_id


def test_task_service_delete_task(session):
    """Test deleting a task using the TaskService."""
    # Create a task
    task_data = TaskCreateRequest(title="Task to Delete", description="Will be deleted")

    user_id = "user123"

    created_task = TaskService.create_task(
        session=session,
        task_data=task_data,
        user_id=user_id
    )

    # Verify the task exists
    retrieved_task = TaskService.get_task_by_id(
        session=session,
        task_id=created_task.id,
        user_id=user_id
    )
    assert retrieved_task.id == created_task.id

    # Delete the task
    result = TaskService.delete_task(
        session=session,
        task_id=created_task.id,
        user_id=user_id
    )

    assert result is True

    # Verify the task no longer exists
    from sqlalchemy.exc import NoResultFound
    from sqlmodel import select

    statement = select(Task).where(Task.id == created_task.id).where(Task.user_id == user_id)
    result = session.exec(statement).first()
    assert result is None


def test_task_service_toggle_completion(session):
    """Test toggling task completion using the TaskService."""
    # Create a task
    task_data = TaskCreateRequest(title="Toggle Task", completed=False)

    user_id = "user123"

    created_task = TaskService.create_task(
        session=session,
        task_data=task_data,
        user_id=user_id
    )

    assert created_task.completed is False

    # Toggle the task completion
    toggled_task = TaskService.toggle_task_completion(
        session=session,
        task_id=created_task.id,
        user_id=user_id
    )

    assert toggled_task.completed is True

    # Toggle again
    toggled_again_task = TaskService.toggle_task_completion(
        session=session,
        task_id=created_task.id,
        user_id=user_id
    )

    assert toggled_again_task.completed is False