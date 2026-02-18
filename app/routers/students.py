from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from ..database import get_session
from ..models import Student, StudentCreate, StudentUpdate
from .. import crud

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(data: StudentCreate, session: Session = Depends(get_session)):
    """Создание нового студента"""
    if crud.get_student_by_email(session, data.email):
        raise HTTPException(status_code=400, detail="Email уже занят")
    return crud.create_student(session, data)


@router.get("/", response_model=List[Student])
def get_all_students(session: Session = Depends(get_session)):
    """Список всех студентов"""
    return crud.get_all_students(session)


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int, session: Session = Depends(get_session)):
    """Студент по ID"""
    student = crud.get_student_by_id(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, data: StudentUpdate, session: Session = Depends(get_session)):
    """Обновление данных студента"""
    student = crud.update_student(session, student_id, data)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, session: Session = Depends(get_session)):
    """Удаление студента (профиль удалится автоматически через CASCADE)"""
    if not crud.delete_student(session, student_id):
        raise HTTPException(status_code=404, detail="Студент не найден")
