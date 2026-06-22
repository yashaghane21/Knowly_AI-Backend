from fastapi import APIRouter, HTTPException

from schemas.auth import RegisterRequest, LoginRequest
from services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(data: RegisterRequest):
    try:
        return AuthService.register_user(
            data.name,
            data.email,
            data.password
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(data: LoginRequest):
    try:
        return AuthService.login_user(
            data.email,
            data.password
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))