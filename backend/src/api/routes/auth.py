from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from fastapi.security import OAuth2PasswordRequestForm
from src.config.database import get_session
from src.services.user_service import UserService
from src.models.user import UserCreate, UserLogin, UserPublic, Token
from src.config.security import create_access_token, get_current_user as get_current_user_from_token
from datetime import timedelta
from src.config.settings import settings


router = APIRouter()


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    session: Session = Depends(get_session)
):
    """Register a new user."""
    try:
        user = UserService.create_user(session, user_data)
        return UserPublic(
            id=user.id,
            email=user.email,
            username=user.username,
            is_active=user.is_active,
            created_at=user.created_at
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/login", response_model=Token)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    """Authenticate user and return access token."""
    # Try authenticating with email first, then username
    user = UserService.authenticate_user(
        session,
        form_data.username,  # This can be email or username
        form_data.password
    )

    # If authentication failed and it looks like an email, try username
    if not user:
        # Check if the input looks like an email
        if '@' in form_data.username:
            # It was an email, so no need to retry with username
            pass
        else:
            # It was probably a username, try again as email
            user = UserService.authenticate_user(
                session,
                form_data.username,
                form_data.password
            )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = UserService.create_access_token_for_user(user)

    return Token(access_token=access_token)


@router.post("/token", response_model=Token)
async def login_user_alt(
    user_login: UserLogin,
    session: Session = Depends(get_session)
):
    """Alternative login endpoint that accepts JSON body."""
    user = UserService.authenticate_user(
        session,
        user_login.email,
        user_login.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = UserService.create_access_token_for_user(user)

    return Token(access_token=access_token)


@router.get("/me", response_model=UserPublic)
async def get_current_user_profile(
    current_user_id: str = Depends(get_current_user_from_token),
    session: Session = Depends(get_session)
):
    """Get current user profile."""
    user = UserService.get_user_by_id(session, current_user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return UserPublic(
        id=user.id,
        email=user.email,
        username=user.username,
        is_active=user.is_active,
        created_at=user.created_at
    )