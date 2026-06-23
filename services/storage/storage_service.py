from abc import ABC, abstractmethod


class StorageService(ABC):

    @abstractmethod
    def upload_file(self, file):
        pass

    @abstractmethod
    def read_file(self, storage_key):
        
        pass

    @abstractmethod
    def delete_file(self, storage_key):
        pass