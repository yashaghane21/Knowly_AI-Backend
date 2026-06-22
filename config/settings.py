from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
JWT_SECRET_KEY="9f3d7a8c2e4b1f6d8a7e5c9f1b3d6a8e4f2c7d9a1e5b8c3d7f4a6b9c2e8d1f5"