from services.integrations.base_connector import (
    BaseConnector
)


class GmailConnector(
    BaseConnector
):

    def authenticate(self):
        pass

    def list_sources(self):
        pass

    def fetch(
        self,
        source_id: str
    ):
        pass

    def sync(self):
        pass

    def disconnect(self):
        pass