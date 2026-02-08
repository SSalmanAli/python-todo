from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from passlib.context import CryptContext
import uuid


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserBase(SQLModel):
    """Base class for User model with common fields."""
    email: str = Field(unique=True, index=True, max_length=255)
    username: str = Field(unique=True, index=True, max_length=255)


class User(UserBase, table=True):
    """User model representing an authenticated user."""
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    hashed_password: str = Field(max_length=255)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str = Field(min_length=8)  # Length validation happens in hash_password


class UserLogin(SQLModel):
    """Schema for user login."""
    email: str = Field(max_length=255)
    password: str = Field(min_length=8)  # Length validation happens in hash_password


class UserPublic(UserBase):
    """Public representation of a user (without sensitive data)."""
    id: str
    is_active: bool
    created_at: datetime


class Token(SQLModel):
    """Authentication token response."""
    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    """Data contained in a token."""
    user_id: str


def hash_password(password: str) -> str:
    """Hash a password with bcrypt, truncating if necessary."""
    # Bcrypt has a 72-byte password limit
    if len(password.encode('utf-8')) > 72:
        # Truncate to 72 bytes and decode back to string
        password = password.encode('utf-8')[:72].decode('utf-8', errors='ignore')
    return pwd_context.hash(password)