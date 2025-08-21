from ..db.database import Base

from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    profession = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(25), nullable=False)
    photo_url = Column(String(255), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
