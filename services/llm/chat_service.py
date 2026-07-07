from google import genai
from google.genai import errors

from config.settings import GEMINI_API_KEY

from services.retrieval.retrieval_service import (
    RetrievalService
)


class ChatService:

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.retrieval_service = RetrievalService()

    def ask(
        self,
        question: str,
        user_id: str
    ):

        retrieved_chunks = self.retrieval_service.search(
            question=question,
            user_id=user_id,
            limit=5
        )

        if not retrieved_chunks:
            return {
                "answer": (
                    "I could not find relevant information "
                    "in your uploaded documents."
                ),
                "sources": []
            }

        context = "\n\n".join(
            [
                f"[Source {index + 1}]\n"
                f"{chunk['text']}"
                for index, chunk in enumerate(
                    retrieved_chunks
                )
            ]
        )

        prompt = f"""
You are Knowly AI, a helpful knowledge assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Do not invent facts.
- If the answer is not in the context, say:
  "I could not find this information in your uploaded documents."
- Give a concise, clear answer.
- Mention source numbers like [Source 1] when useful.

Context:
{context}

User question:
{question}
"""

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        except errors.ClientError as error:

            if error.code == 429:
                return {
                    "answer": (
                        "The AI service has reached its request limit. "
                        "Please try again shortly."
                    ),
                    "sources": self._format_sources(
                        retrieved_chunks
                    ),
                    "error_code": "LLM_RATE_LIMITED"
                }

            raise

        except errors.ServerError as error:

            if error.code == 503:
                return {
                    "answer": (
                        "The AI model is temporarily busy. "
                        "Please try again in a few seconds."
                    ),
                    "sources": self._format_sources(
                        retrieved_chunks
                    ),
                    "error_code": "LLM_UNAVAILABLE"
                }

            raise

        return {
            "answer": response.text,
            "sources": self._format_sources(
                retrieved_chunks
            )
        }

    @staticmethod
    def _format_sources(
        retrieved_chunks
    ):

        return [
            {
                "document_id": chunk["document_id"],

                "chunk_index": chunk["chunk_index"],

                "score": round(
                    chunk["score"],
                    3
                )
            }
            for chunk in retrieved_chunks
        ]