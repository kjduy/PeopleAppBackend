from ..db.database import get_db
from ..models.person import Person
from ..schemas.person import PersonOut
from ..services.storage import save_photo

from datetime import date
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session


router = APIRouter(prefix="/persons", tags=["persons"])


@router.post("/", response_model=PersonOut)
async def create_person(
    first_name: str = Form(...),
    last_name: str = Form(...),
    birth_date: date = Form(...),
    age: int = Form(...),
    profession: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    photo: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    photo_url = save_photo(photo)
    person = Person(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        age=age,
        profession=profession,
        address=address,
        phone=phone,
        photo_url=photo_url,
    )
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@router.get("/", response_model=list[PersonOut])
async def list_persons(db: Session = Depends(get_db)):
    return db.query(Person).order_by(Person.created_at.desc()).all()
