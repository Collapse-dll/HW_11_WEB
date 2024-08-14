from sqlalchemy import Column, Integer, String, func, Date
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(13), nullable=False)
    birth_date = Column(Date, nullable=False)
    additional_info = Column(String(250), nullable=True)
    created_at = Column("created_at", DateTime, default=func.now())

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 13:
            raise ValueError("Phone number must be 13 characters long")
        return phone_number