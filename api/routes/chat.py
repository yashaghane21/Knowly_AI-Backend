from fastapi import (
    APIRouter,
    Depends
)

from pydantic import BaseModel

from services.llm.chat_service import (
    ChatService
)

from utils.dependencies import (
    get_current_user
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

chat_service = ChatService()
class AskQuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(
    request: AskQuestionRequest,
    current_user=Depends(get_current_user)
):

    return chat_service.ask(
        question=request.question,
        user_id=str(current_user["_id"])
    )