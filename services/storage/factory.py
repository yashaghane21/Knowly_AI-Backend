from services.storage.local_storage_service import (
    LocalStorageService
)


class StorageFactory:

    @staticmethod
    def get_storage():

        return LocalStorageService()