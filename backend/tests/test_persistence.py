"""
Test for data persistence across application restarts.
This test simulates the scenario where data needs to survive server restarts.
"""

import pytest
from sqlmodel import Session, select
from src.models.task import Task
from src.config.database import engine


def test_data_persistence():
    """
    Test that data persists across different sessions.
    This simulates data surviving application restarts by using separate sessions.
    """
    # Create a task in one session
    task_title = "Persistence Test Task"
    task_description = "This task should persist across sessions"
    user_id = "persistent_user"

    # Session 1: Create the task
    with Session(engine) as session1:
        task = Task(
            title=task_title,
            description=task_description,
            completed=False,
            user_id=user_id
        )
        session1.add(task)
        session1.commit()
        session1.refresh(task)

        original_task_id = task.id
        assert original_task_id is not None

    # Session 2: Verify the task still exists
    with Session(engine) as session2:
        retrieved_task = session2.get(Task, original_task_id)

        assert retrieved_task is not None
        assert retrieved_task.id == original_task_id
        assert retrieved_task.title == task_title
        assert retrieved_task.description == task_description
        assert retrieved_task.user_id == user_id
        assert retrieved_task.completed is False


def test_multiple_data_persistence():
    """Test persistence of multiple tasks."""
    user_id = "multi_persist_user"

    # Create multiple tasks in one session
    tasks_to_create = [
        {"title": "Task 1", "description": "First persistent task", "completed": False},
        {"title": "Task 2", "description": "Second persistent task", "completed": True},
        {"title": "Task 3", "description": "Third persistent task", "completed": False},
    ]

    task_ids = []

    # Session 1: Create tasks
    with Session(engine) as session1:
        for task_data in tasks_to_create:
            task = Task(
                title=task_data["title"],
                description=task_data["description"],
                completed=task_data["completed"],
                user_id=user_id
            )
            session1.add(task)
            session1.commit()
            session1.refresh(task)
            task_ids.append(task.id)

    # Verify all tasks were created with IDs
    assert len(task_ids) == len(tasks_to_create)
    assert all(task_id is not None for task_id in task_ids)

    # Session 2: Verify all tasks still exist
    with Session(engine) as session2:
        for i, task_id in enumerate(task_ids):
            retrieved_task = session2.get(Task, task_id)

            assert retrieved_task is not None
            assert retrieved_task.id == task_id
            assert retrieved_task.title == tasks_to_create[i]["title"]
            assert retrieved_task.description == tasks_to_create[i]["description"]
            assert retrieved_task.completed == tasks_to_create[i]["completed"]
            assert retrieved_task.user_id == user_id


def test_user_isolation_persistence():
    """Test that user isolation is maintained across sessions."""
    user1_id = "user1_persist"
    user2_id = "user2_persist"

    # Session 1: Create tasks for different users
    with Session(engine) as session1:
        # User 1's tasks
        task1_user1 = Task(title="User1 Task1", description="Owned by user1", completed=False, user_id=user1_id)
        task2_user1 = Task(title="User1 Task2", description="Owned by user1", completed=True, user_id=user1_id)

        # User 2's tasks
        task1_user2 = Task(title="User2 Task1", description="Owned by user2", completed=False, user_id=user2_id)
        task2_user2 = Task(title="User2 Task2", description="Owned by user2", completed=True, user_id=user2_id)

        session1.add(task1_user1)
        session1.add(task2_user1)
        session1.add(task1_user2)
        session1.add(task2_user2)
        session1.commit()

        # Refresh to get IDs
        session1.refresh(task1_user1)
        session1.refresh(task2_user1)
        session1.refresh(task1_user2)
        session1.refresh(task2_user2)

        user1_task_ids = [task1_user1.id, task2_user1.id]
        user2_task_ids = [task1_user2.id, task2_user2.id]

    # Session 2: Verify user isolation
    with Session(engine) as session2:
        # Get all tasks for user1
        user1_statement = select(Task).where(Task.user_id == user1_id)
        user1_tasks = session2.exec(user1_statement).all()

        # Get all tasks for user2
        user2_statement = select(Task).where(Task.user_id == user2_id)
        user2_tasks = session2.exec(user2_statement).all()

        # Verify user isolation is maintained
        assert len(user1_tasks) == 2
        assert len(user2_tasks) == 2

        user1_titles = {task.title for task in user1_tasks}
        user2_titles = {task.title for task in user2_tasks}

        assert user1_titles == {"User1 Task1", "User1 Task2"}
        assert user2_titles == {"User2 Task1", "User2 Task2"}

        # Verify no cross-contamination
        all_user1_task_titles = [task.title for task in user1_tasks]
        all_user2_task_titles = [task.title for task in user2_tasks]

        for title in all_user1_task_titles:
            assert "User1" in title

        for title in all_user2_task_titles:
            assert "User2" in title