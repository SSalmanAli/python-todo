from datetime import timedelta
from src.config.security import create_access_token

# Data to encode in the token
user_data = {"sub": "user_id_123"}

# Generate token with expiration time
token = create_access_token(data=user_data, expires_delta=timedelta(minutes=60))
print(token)