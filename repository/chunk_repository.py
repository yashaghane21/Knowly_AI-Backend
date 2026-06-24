from bson import ObjectId

from db.mongodb import db


class ChunkRepository:

    @staticmethod
    def create_many(chunks):
        return db.chunks.insert_many(chunks)

    @staticmethod
    def get_by_document_id(
        document_id: str
    ):
        return list(
            db.chunks.find(
                {
                    "documentId": document_id
                }
            )
        )

    @staticmethod
    def update_embedding(
        chunk_id: str,
        embedding: list[float]
    ):
        return db.chunks.update_one(
            {
                "_id": ObjectId(chunk_id)
            },
            {
                "$set": {
                    "embedding": embedding
                }
            }
        )