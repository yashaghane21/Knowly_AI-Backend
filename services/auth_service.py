from datetime import datetime

from repository.user_repository import UserRepository
from utils.security import hash_password, verify_password

from utils.jwt_handler import create_access_token

class AuthService:

    @staticmethod
    def register_user(name: str, email: str, password: str):

        existing_user = UserRepository.find_by_email(email)

        if existing_user:
            raise Exception("User already exists")

        user_data = {
            "name": name,
            "email": email,
            "password": hash_password(password),
            "createdAt": datetime.utcnow()
        }

        UserRepository.create_user(user_data)

        return {
            "message": "User registered successfully"
        }

    @staticmethod
    def login_user(email: str, password: str):

        user = UserRepository.find_by_email(email)

        if not user:
            raise Exception("Invalid credentials")

        if not verify_password(password, user["password"]):
            raise Exception("Invalid credentials")

        token = create_access_token(
    {
        "user_id": str(user["_id"]),
        "email": user["email"]
    }
)

        return {
            "access_token": token,
            "token_type": "bearer"
        }