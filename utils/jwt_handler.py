from datetime import datetime, timedelta
from jose import jwt

from config.settings import JWT_SECRET_KEY

ALGORITHM = "HS256"


def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(days=1)

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )