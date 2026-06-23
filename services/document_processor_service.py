import fitz

from datetime import datetime

from repository.document_repository import (
    DocumentRepository
)

from repository.knowledge_source_repository import (
    KnowledgeSourceRepository
)

from services.storage.factory import (
    StorageFactory
)



class DocumentProcessorService:

    @staticmethod
    def process_pdf(source_id: str):

        source = (
            KnowledgeSourceRepository.get_by_id(
                source_id
            )
        )

        if not source:
            raise Exception(
                "Knowledge source not found"
            )
        
        storage = StorageFactory.get_storage()

        pdf_path = storage.read_file(
            source["metadata"]["storageKey"]
        )

        pdf = fitz.open(pdf_path)

        full_text = ""

        for page in pdf:
            full_text += page.get_text()

        document_data = {
            "sourceId": str(source["_id"]),

            "userId": source["userId"],

            "title": source["sourceName"],

            "content": full_text,

            "createdAt": datetime.utcnow()
        }

        DocumentRepository.create(
            document_data
        )

        KnowledgeSourceRepository.update_status(
            source_id,
            "processed"
        )

        # print("hii yash aghane ",full_text)

        return {
            "message": "Document processed",
            "characters": len(full_text)
        }