from datetime import date, datetime
from pydantic import BaseModel, Field


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    age: int = Field(ge=0)
    profession: str
    address: str
    phone: str


class PersonOut(PersonBase):
    id: int
    photo_url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
