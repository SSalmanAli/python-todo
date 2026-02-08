from sqlmodel import Session, select
from typing import Optional
from src.models.user import User, UserCreate, pwd_context, hash_password
from src.utils.token_utils import create_access_token
from datetime import timedelta
from src.config.settings import settings


class UserService:
    """Service class for user-related operations."""

    @staticmethod
    def get_user_by_email(session: Session, email: str) -> Optional[User]:
        """Get a user by email."""
        statement = select(User).where(User.email == email)
        return session.exec(statement).first()

    @staticmethod
    def get_user_by_username(session: Session, username: str) -> Optional[User]:
        """Get a user by username."""
        statement = select(User).where(User.username == username)
        return session.exec(statement).first()

    @staticmethod
    def get_user_by_id(session: Session, user_id: str) -> Optional[User]:
        """Get a user by ID."""
        statement = select(User).where(User.id == user_id)
        return session.exec(statement).first()

    @staticmethod
    def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
        """Authenticate a user by email and password."""
        user = UserService.get_user_by_email(session, email)
        if not user or not pwd_context.verify(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_user(session: Session, user_data: UserCreate) -> User:
        """Create a new user."""
        # Check if user with email already exists
        existing_user = UserService.get_user_by_email(session, user_data.email)
        if existing_user:
            raise ValueError("Email already registered")

        # Check if user with username already exists
        existing_username = UserService.get_user_by_username(session, user_data.username)
        if existing_username:
            raise ValueError("Username already taken")

        # Hash the password
        hashed_password = hash_password(user_data.password)

        # Create the user
        user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_password
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        return user

    @staticmethod
    def create_access_token_for_user(user: User) -> str:
        """Create an access token for a user."""
        data = {"sub": user.id}
        expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return create_access_token(data=data, expires_delta=expires)