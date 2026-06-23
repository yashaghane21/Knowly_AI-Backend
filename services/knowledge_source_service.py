import os
import uuid

from datetime import datetime

from repository.knowledge_source_repository import (
    KnowledgeSourceRepository
)


class KnowledgeSourceService:

    @staticmethod
    def upload_pdf(
        file,
        current_user
    ):

        extension = file.filename.split(".")[-1]

        unique_name = f"{uuid.uuid4()}.{extension}"

        file_path = os.path.join(
            "uploads",
            unique_name
        )

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        source_data = {
            "userId": str(current_user["_id"]),

            "sourceType": "pdf",

            "sourceName": file.filename,

            "status": "uploaded",

            "metadata": {
                "filePath": file_path,
                "fileSize": os.path.getsize(file_path)
            },

            "createdAt": datetime.utcnow()
        }

        result = KnowledgeSourceRepository.create(
            source_data
        )

        return {
            "source_id": str(result.inserted_id),
            "status": "uploaded"
        }