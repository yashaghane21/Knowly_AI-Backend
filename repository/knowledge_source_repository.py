from bson import ObjectId
from db.mongodb import db


class KnowledgeSourceRepository:

    @staticmethod
    def create(source_data: dict):
        return db.knowledge_sources.insert_one(source_data)

    @staticmethod
    def get_by_user(user_id: str):
        return list(
            db.knowledge_sources.find(
                {"userId": user_id}
            )
        )

    @staticmethod
    def get_by_id(source_id: str):
        return db.knowledge_sources.find_one(
            {"_id": ObjectId(source_id)}
        )

    @staticmethod
    def update_status(
        source_id: str,
        status: str
    ):
        db.knowledge_sources.update_one(
            {"_id": ObjectId(source_id)},
            {"$set": {"status": status}}
        )