from db.mongodb import db


class KnowledgeSourceRepository:

    @staticmethod
    def create(source_data: dict):
        return db.knowledge_sources.insert_one(
            source_data
        )

    @staticmethod
    def get_by_user(user_id: str):
        return list(
            db.knowledge_sources.find(
                {"userId": user_id}
            )
        )