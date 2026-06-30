from abc import ABC,abstractmethod

class BaseConnector(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    def list_resource(self):
        pass

    def fetch(self):
        pass
    def sync(self):
        pass
    def disconnect(self):
        pass