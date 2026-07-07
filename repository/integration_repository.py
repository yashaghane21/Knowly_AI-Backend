from db.mongodb import db


class IntegrationRepository:

    @staticmethod
    def create(data: dict):
        return db.integrations.insert_one(data)

    @staticmethod
    def find_by_user_and_provider(
        user_id: str,
        provider: str
    ):
        return db.integrations.find_one({
            "userId": user_id,
            "provider": provider
        })

    @staticmethod
    def update_tokens(
        user_id: str,
        provider: str,
        update_data: dict
    ):
        return db.integrations.update_one(
            {
                "userId": user_id,
                "provider": provider
            },
            {
                "$set": update_data
            },
            upsert=True
        )