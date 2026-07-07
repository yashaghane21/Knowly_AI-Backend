from datetime import datetime

from repository.knowledge_source_repository import (
    KnowledgeSourceRepository
)

from services.storage.factory import (
    StorageFactory
)

from services.ingestion.document_processor_service import DocumentProcessorService
from services.ingestion.ingestion_pipeline_service import (
    IngestionPipelineService
)

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

        source_id = str(
            result.inserted_id
        )

        IngestionPipelineService.run(           # call ingestion pipeline 
            source_id
        )


        return {
            "source_id": str(result.inserted_id),
            "status": "uploaded"
        }