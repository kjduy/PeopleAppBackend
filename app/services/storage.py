import uuid

from ..db.config import settings

from fastapi import UploadFile
from pathlib import Path


UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_photo(file: UploadFile) -> str:
    ext = Path(file.filename).suffix.lower()
    name = f"{uuid.uuid4().hex}{ext}"
    dest = UPLOAD_DIR / name
    with dest.open("wb") as f:
        f.write(file.file.read())
    return f"/{settings.UPLOAD_DIR}/{name}"
