from db.mongodb import db


class DocumentRepository:

    @staticmethod
    def create(document_data: dict):
        return db.documents.insert_one(document_data)

    @staticmethod
    def find_by_source_id(source_id: str):
        return db.documents.find_one(
            {"sourceId": source_id}
        )