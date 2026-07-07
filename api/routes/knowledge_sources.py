from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from utils.dependencies import get_current_user

from services.knowledge.knowledge_source_service import (
    KnowledgeSourceService
)

router = APIRouter(
    prefix="/knowledge-sources",
    tags=["Knowledge Sources"]
)


@router.post("/upload")
def upload_pdf(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    return KnowledgeSourceService.upload_pdf(
        file,
        current_user
    )