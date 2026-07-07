from services.ingestion.document_processor_service import (
    DocumentProcessorService
)

from services.ingestion.chunking_service import (
    ChunkingService
)

from services.embeddings.embedding_service import (
    EmbeddingService
)


class IngestionPipelineService:

    @staticmethod
    def run(source_id: str):

        document_result = (
            DocumentProcessorService.process_pdf(
                source_id
            )
        )

        document_id = document_result["document_id"]

        chunk_result = (
            ChunkingService.process_document(
                document_id
            )
        )

        embedding_result = (
            EmbeddingService().process_document(
                document_id
            )
        )

        return {
            "status": "processed",
            "document_id": document_id,
            "chunks_created": chunk_result[
                "chunks_created"
            ],
            "embeddings_created": embedding_result[
                "embeddings_created"
            ]
        }