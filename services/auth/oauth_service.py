from google_auth_oauthlib.flow import Flow

from config.settings import (
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
    GOOGLE_REDIRECT_URI
)

from services.auth.oauth_state import (
    OAuthStateStore
)
class OAuthService:

    SCOPES = [
        "openid",
        "email",
        "profile",
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/gmail.readonly"
    ]

    @staticmethod
    def get_flow():

        return Flow.from_client_config(
            {
                "web": {
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "auth_uri":
                        "https://accounts.google.com/o/oauth2/auth",
                    "token_uri":
                        "https://oauth2.googleapis.com/token"
                }
            },
            scopes=OAuthService.SCOPES,
            redirect_uri=GOOGLE_REDIRECT_URI
        )
    
    @staticmethod
    def get_authorization_url(
        user_id: str
    ):

        flow = OAuthService.get_flow()
        state = OAuthStateStore.create(
    user_id
)

        authorization_url, _ = flow.authorization_url(
    state=state,
    access_type="offline",
    include_granted_scopes="true",
    prompt="consent"
)

        return {
            "authorization_url": authorization_url,
            "state": state
        }


    @staticmethod
    def exchange_code(code: str):
    
        flow = OAuthService.get_flow()
    
        flow.fetch_token(code=code)
    
        credentials = flow.credentials
    
        return {
            "access_token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "expiry": credentials.expiry,
            "scopes": credentials.scopes
        }    