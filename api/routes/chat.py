from fastapi import (
    APIRouter,
    Depends
)

from pydantic import BaseModel

from services.chat_service import (
    ChatService
)

from utils.dependencies import (
    get_current_user
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class AskQuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(
    request: AskQuestionRequest,
    current_user=Depends(get_current_user)
):

    chat_service = ChatService()

    return chat_service.ask(
        question=request.question,
        user_id=str(current_user["_id"])
    )