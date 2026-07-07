from fastapi import FastAPI
from api.routes.auth import router as auth_router  
from api.routes.chat import (
    router as chat_router
)
from api.routes.knowledge_sources import router as knowledge_router
from api.routes.integrations.google import router as integrations_router
from utils.dependencies import get_current_user
from fastapi import Depends

app = FastAPI(
    title="Knowly AI",
    version="1.0.0"
)




@app.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "id": str(current_user["_id"]),
        "name": current_user["name"],
        "email": current_user["email"]
    }




app.include_router(auth_router)
app.include_router(knowledge_router)
app.include_router(chat_router)
@app.get("/")
def root():
    return {
        "message": "Knowly AI Backend Running"
    }
app.include_router(integrations_router)