from fastapi import FastAPI
from api.routes.auth import router as auth_router

app = FastAPI(
    title="Knowly AI",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Knowly AI Backend Running"
    }