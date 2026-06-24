from datetime import datetime

from repository.document_repository import (
    DocumentRepository
)

from repository.chunk_repository import (
    ChunkRepository
)


class ChunkingService:

    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100

    @staticmethod
    def process_document(
        document_id: str
    ):

        document = (
            DocumentRepository.find_by_id(
                document_id
            )
        )

        if not document:
            raise Exception(
                "Document not found"
            )

        content = document["content"]

        chunks = []

        start = 0
        chunk_index = 0

        while start < len(content):

            end = (
                start
                +
                ChunkingService.CHUNK_SIZE
            )

            chunk_text = content[start:end]

            chunks.append({
                "documentId": document_id,

                "userId": document["userId"],

                "chunkIndex": chunk_index,

                "chunkText": chunk_text,

                "createdAt": datetime.utcnow()
            })

            start += (
                ChunkingService.CHUNK_SIZE
                -
                ChunkingService.CHUNK_OVERLAP
            )

            chunk_index += 1

        ChunkRepository.create_many(
            chunks
        )

        return {
            "document_id": document_id,

            "chunks_created": len(chunks)
        }