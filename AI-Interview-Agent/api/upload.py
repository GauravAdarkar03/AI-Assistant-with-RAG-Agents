import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.rag_service import RAGService

router = APIRouter()


@router.post("/upload")

async def upload_resume(
        file: UploadFile = File(...)
):

    os.makedirs("data", exist_ok=True)

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = RAGService.process_pdf(file_path)

    return result