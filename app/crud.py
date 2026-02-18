from sqlmodel import Session, select
from typing import List, Optional

from .models import (
    Student, StudentCreate, StudentUpdate,
    UserProfile, UserProfileCreate, UserProfileUpdate,
)


# ──────────────────────────────────────────────
# Students CRUD
# ──────────────────────────────────────────────

def create_student(session: Session, data: StudentCreate) -> Student:
    student = Student(**data.model_dump())
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def get_all_students(session: Session) -> List[Student]:
    return session.exec(select(Student)).all()

def get_student_by_id(session: Session, student_id: int) -> Optional[Student]:
    return session.get(Student, student_id)

def get_student_by_email(session: Session, email: str) -> Optional[Student]:
    return session.exec(select(Student).where(Student.email == email)).first()

def update_student(session: Session, student_id: int, data: StudentUpdate) -> Optional[Student]:
    student = session.get(Student, student_id)
    if student:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(student, key, value)
        session.add(student)
        session.commit()
        session.refresh(student)
    return student

def delete_student(session: Session, student_id: int) -> bool:
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        return True
    return False


# ──────────────────────────────────────────────
# UserProfile CRUD
# ──────────────────────────────────────────────

def create_user_profile(session: Session, student_id: int, data: UserProfileCreate) -> UserProfile:
    profile = UserProfile(student_id=student_id, **data.model_dump())
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile

def get_user_profile(session: Session, student_id: int) -> Optional[UserProfile]:
    return session.get(UserProfile, student_id)

def update_user_profile(session: Session, student_id: int, data: UserProfileUpdate) -> Optional[UserProfile]:
    profile = session.get(UserProfile, student_id)
    if profile:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(profile, key, value)
        session.add(profile)
        session.commit()
        session.refresh(profile)
    return profile

def delete_user_profile(session: Session, student_id: int) -> bool:
    profile = session.get(UserProfile, student_id)
    if profile:
        session.delete(profile)
        session.commit()
        return True
    return False
