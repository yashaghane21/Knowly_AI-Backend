from datetime import datetime

from repository.knowledge_source_repository import (
    KnowledgeSourceRepository
)

from services.storage.factory import (
    StorageFactory
)

from services.document_processor_service import DocumentProcessorService


class KnowledgeSourceService:

    @staticmethod
    def upload_pdf(
        file,
        current_user
    ):

        storage = StorageFactory.get_storage()

        file_info = storage.upload_file(file)

        source_data = {
            "userId": str(current_user["_id"]),

            "sourceType": "pdf",

            "sourceName": file.filename,

            "status": "uploaded",

            "metadata": {
                "storageProvider":
                    file_info["storageProvider"],

                "storageKey":
                    file_info["storageKey"],

                "fileSize":
                    file.file.tell()
            },

            "createdAt": datetime.utcnow()
        }

        result = KnowledgeSourceRepository.create(
            source_data
        )

        DocumentProcessorService.process_pdf(
        str(result.inserted_id)
)


        return {
            "source_id": str(result.inserted_id),
            "status": "uploaded"
        }