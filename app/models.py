from sqlmodel import SQLModel, Field
from datetime import date, datetime
from typing import Optional


class Student(SQLModel, table=True):
    __tablename__ = "students"

    student_id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(max_length=100, unique=True, nullable=False)
    phone: Optional[str] = Field(default=None, max_length=20, unique=True)
    registration_date: date = Field(
        default_factory=date.today,
        nullable=False
    )

    class Config:
        schema_extra = {
            "example": {
                "email": "student@example.com",
                "phone": "+1234567890",
                "registration_date": "2024-01-15"
            }
        }


# Модель для создания студента (без ID и с опциональной датой)
class StudentCreate(SQLModel):
    email: str
    phone: Optional[str] = None
    registration_date: Optional[date] = Field(default_factory=date.today)


# Модель для обновления студента
class StudentUpdate(SQLModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    registration_date: Optional[date] = None