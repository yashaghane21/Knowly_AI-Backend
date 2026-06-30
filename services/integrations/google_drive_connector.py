from services.integrations import base_connector

class GoogleDriveConnector(
    base_connector
):

  def authenticate(self):
    pass
  
  def list_resource(self):
    pass
  
  def fetch(self,source_id:str):
    pass
  
  def sync(self):
    pass
  
  def disconnect(self):
    pass