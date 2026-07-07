from db.mongodb import db

from services.embedding_model import (
    EmbeddingModel
)


class RetrievalService:

    def __init__(self):
        self.model = EmbeddingModel.get_model()

    def search(
        self,
        question: str,
        user_id: str,
        limit: int = 5
    ):

        query_embedding = self.model.encode(
            question
        ).tolist()

        pipeline = [
            {
                "$vectorSearch": {
                    "index": "chunk_vector_index",

                    "path": "embedding",

                    "queryVector": query_embedding,

                    "numCandidates": 100,

                    "limit": limit,

                    "filter": {
                        "userId": user_id
                    }
                }
            },
            {
                "$project": {
                    "_id": 1,

                    "documentId": 1,

                    "chunkIndex": 1,

                    "chunkText": 1,

                    "score": {
                        "$meta": "vectorSearchScore"
                    }
                }
            }
        ]

        results = list(
            db.chunks.aggregate(
                pipeline
            )
        )

        unique_results = []
        seen = set()

        for result in results:

            unique_key = (
                result["documentId"],
                result["chunkIndex"]
            )

            if unique_key in seen:
                continue

            seen.add(unique_key)

            unique_results.append({
                "chunk_id": str(result["_id"]),

                "document_id": result["documentId"],

                "chunk_index": result["chunkIndex"],

                "text": result["chunkText"],

                "score": result["score"]
            })

        return unique_results