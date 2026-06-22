from db.mongodb import db


class UserRepository:

    @staticmethod
    def find_by_email(email: str):
        return db.users.find_one({"email": email})

    @staticmethod
    def create_user(user_data: dict):
        return db.users.insert_one(user_data)

    @staticmethod
    def find_by_id(user_id):
        return db.users.find_one({"_id": user_id})