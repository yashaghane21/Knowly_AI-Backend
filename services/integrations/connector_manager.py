from services.integrations.google_drive_connector import GoogleDriveConnector
from services.integrations.gmail_connector import GmailConnector


class ConnectorManager:
    @staticmethod 
    def get_connector(provider:str):

        if(provider=="google_drive"):
            return GoogleDriveConnector()
        
        
        if provider == "gmail":
            return GmailConnector()

        raise Exception(
            "Unsupported connector"
        )
    