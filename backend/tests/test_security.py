import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from unittest.mock import patch
from src.config.security import verify_token, verify_user_access, create_access_token


def test_jwt_token_creation():
    """Test creating a JWT token."""
    data = {"sub": "user123"}
    token = create_access_token(data=data)

    # Verify the token can be decoded
    decoded = verify_token(token)
    assert decoded["sub"] == "user123"
    assert decoded["type"] == "access"


def test_jwt_token_verification():
    """Test verifying a valid JWT token."""
    data = {"sub": "user123"}
    token = create_access_token(data=data)

    decoded = verify_token(token)
    assert decoded["sub"] == "user123"


def test_jwt_token_verification_with_invalid_token():
    """Test verifying an invalid JWT token."""
    with pytest.raises(HTTPException) as exc_info:
        verify_token("invalid.token.here")

    assert exc_info.value.status_code == 401
    assert "could not validate credentials" in exc_info.value.detail.lower()


def test_user_access_verification():
    """Test user access verification function."""
    # Same user should have access
    assert verify_user_access("user123", "user123") is True

    # Different users should not have access
    assert verify_user_access("user123", "user456") is False


def test_api_endpoint_with_valid_jwt(client):
    """Test accessing an API endpoint with a valid JWT token."""
    # Mock JWT token validation
    with patch("src.config.security.verify_token", return_value={"sub": "user123", "type": "access"}):
        response = client.get("/health", headers={"Authorization": "Bearer valid-token"})
        assert response.status_code == 200


def test_api_endpoint_without_jwt(client):
    """Test accessing an API endpoint without a JWT token."""
    response = client.get("/health")  # No Authorization header
    assert response.status_code == 403  # FastAPI will return 403 if security scheme is required


def test_task_endpoints_require_authentication(client):
    """Test that task endpoints require authentication."""
    # Try to access task endpoints without authentication
    endpoints = [
        "/tasks/",
        "/tasks/1",
        "/tasks/1/toggle"
    ]

    for endpoint in endpoints:
        response = client.get(endpoint)
        # Should return 403 (forbidden) or 422 (validation error for missing header)
        # depending on FastAPI's handling of missing security headers
        assert response.status_code in [403, 422, 401]