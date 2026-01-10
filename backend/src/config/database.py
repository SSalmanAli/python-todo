from sqlmodel import create_engine, Session
from typing import Generator
from src.config.settings import settings


# Create the database engine for NeonDB with pg8000 driver
# pg8000 is a pure Python PostgreSQL driver that works well with NeonDB
engine = create_engine(
    settings.DATABASE_URL,
    echo=False  # Set to True to see SQL queries in logs during development
)


def get_session() -> Generator[Session, None, None]:
    """Get database session for dependency injection."""
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    """Create database tables (call this on application startup)."""
    from src.models.task import Task  # Import here to avoid circular imports
    from sqlmodel import SQLModel

    # Create all tables
    SQLModel.metadata.create_all(engine)