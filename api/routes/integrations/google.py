from fastapi import (
    APIRouter,
    Depends
)

from services.auth.oauth_service import (
    OAuthService
)

from utils.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/api/integrations",
    tags=["Google Integration"]
)


@router.get("/google/login")
def google_login(

    current_user=Depends(
        get_current_user
    )

):

    return OAuthService.get_authorization_url(
        user_id=str(
            current_user["_id"]
        )
    )


@router.get("/google/callback")
def google_callback(
    code: str
):

    return OAuthService.exchange_code(
        code
    )