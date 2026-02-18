from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, ForeignKey
from datetime import date
from typing import Optional


# ──────────────────────────────────────────────
# Students
# ──────────────────────────────────────────────

class Student(SQLModel, table=True):
    __tablename__ = "students"

    student_id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(max_length=100, unique=True, nullable=False)
    phone: Optional[str] = Field(default=None, max_length=20, unique=True)
    registration_date: date = Field(default_factory=date.today, nullable=False)


class StudentCreate(SQLModel):
    email: str
    phone: Optional[str] = None
    registration_date: Optional[date] = Field(default_factory=date.today)


class StudentUpdate(SQLModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    registration_date: Optional[date] = None


# ──────────────────────────────────────────────
# UserProfile  — ON DELETE CASCADE + ON UPDATE CASCADE
# Реализовано через явный SQLAlchemy Column,
# так как SQLModel не поддерживает onupdate напрямую
# ──────────────────────────────────────────────

class UserProfile(SQLModel, table=True):
    __tablename__ = "user_profiles"

    student_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            Integer,
            ForeignKey("students.student_id", ondelete="CASCADE", onupdate="CASCADE"),
            primary_key=True,
        ),
    )
    birth_date: Optional[date] = Field(default=None)
    country: Optional[str] = Field(default=None, max_length=50)
    address: Optional[str] = Field(default=None, max_length=150)


class UserProfileCreate(SQLModel):
    birth_date: Optional[date] = None
    country: Optional[str] = None
    address: Optional[str] = None


class UserProfileUpdate(SQLModel):
    birth_date: Optional[date] = None
    country: Optional[str] = None
    address: Optional[str] = None
