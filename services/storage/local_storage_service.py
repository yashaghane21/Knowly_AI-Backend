import os
import uuid

from services.storage.storage_service import (
    StorageService
)


class LocalStorageService(StorageService):

    UPLOAD_DIR = "uploads"

    def upload_file(self, file):

        extension = file.filename.split(".")[-1]

        storage_key = (
            f"{uuid.uuid4()}.{extension}"
        )

        file_path = os.path.join(
            self.UPLOAD_DIR,
            storage_key
        )

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        return {
            "storageProvider": "local",
            "storageKey": storage_key,
            "filePath": file_path
        }

    def read_file(self, storage_key):

        return os.path.join(
            self.UPLOAD_DIR,
            storage_key
        )

    def delete_file(self, storage_key):

        file_path = self.read_file(
            storage_key
        )

        if os.path.exists(file_path):
            os.remove(file_path)