from services.embedding_model import (
    EmbeddingModel
)
from repository.chunk_repository import (
    ChunkRepository
)


class EmbeddingService:

    def __init__(self):
       self.model = EmbeddingModel.get_model()

    def process_document(
        self,
        document_id: str
    ):

        chunks = ChunkRepository.get_by_document_id(
            document_id
        )

        if not chunks:
            raise Exception(
                "No chunks found for this document"
            )

        chunk_texts = [
            chunk["chunkText"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            chunk_texts
        ).tolist()

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):
            ChunkRepository.update_embedding(
                str(chunk["_id"]),
                embedding
            )

        return {
            "document_id": document_id,
            "embeddings_created": len(chunks)
        }