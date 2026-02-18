from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from ..database import get_session
from ..models import Student, StudentCreate, StudentUpdate
from .. import crud

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student_endpoint(
        student_data: StudentCreate,
        session: Session = Depends(get_session)
):
    """Создание нового студента"""
    # Проверка уникальности email
    existing_student = crud.get_student_by_email(session, student_data.email)
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student with this email already exists"
        )

    return crud.create_student(session, student_data)


@router.get("/", response_model=List[Student])
def get_all_students_endpoint(
        session: Session = Depends(get_session)
):
    """Получение списка всех студентов"""
    return crud.get_all_students(session)


@router.get("/{student_id}", response_model=Student)
def get_student_endpoint(
        student_id: int,
        session: Session = Depends(get_session)
):
    """Получение студента по ID"""
    student = crud.get_student_by_id(session, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student


@router.put("/{student_id}", response_model=Student)
def update_student_endpoint(
        student_id: int,
        student_data: StudentUpdate,
        session: Session = Depends(get_session)
):
    """Обновление данных студента"""
    student = crud.update_student(session, student_id, student_data)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student_endpoint(
        student_id: int,
        session: Session = Depends(get_session)
):
    """Удаление студента"""
    deleted = crud.delete_student(session, student_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return None