from sqlmodel import Session, select
from typing import List, Optional
from .models import Student, StudentCreate, StudentUpdate

def create_student(session: Session, student_data: StudentCreate) -> Student:
    """Создание нового студента"""
    student = Student(**student_data.model_dump())
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def get_all_students(session: Session) -> List[Student]:
    """Получение списка всех студентов"""
    statement = select(Student)
    results = session.exec(statement)
    return results.all()

def get_student_by_id(session: Session, student_id: int) -> Optional[Student]:
    """Получение студента по ID"""
    return session.get(Student, student_id)

def update_student(session: Session, student_id: int, student_data: StudentUpdate) -> Optional[Student]:
    """Обновление данных студента"""
    student = session.get(Student, student_id)
    if student:
        update_data = student_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(student, key, value)
        session.add(student)
        session.commit()
        session.refresh(student)
    return student

def delete_student(session: Session, student_id: int) -> bool:
    """Удаление студента"""
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        return True
    return False

def get_student_by_email(session: Session, email: str) -> Optional[Student]:
    """Получение студента по email"""
    statement = select(Student).where(Student.email == email)
    return session.exec(statement).first()