from fastapi import FastAPI
from api.routes.auth import router as auth_router  
from utils.dependencies import get_current_user
from fastapi import Depends
from api.routes.knowledge_sources import router as knowledge_router

app = FastAPI(
    title="Knowly AI",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(knowledge_router)



@app.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "id": str(current_user["_id"]),
        "name": current_user["name"],
        "email": current_user["email"]
    }


@app.get("/")
def root():
    return {
        "message": "Knowly AI Backend Running"
    }