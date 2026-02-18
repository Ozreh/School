from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from ..database import get_session
from ..models import UserProfile, UserProfileCreate, UserProfileUpdate
from .. import crud

router = APIRouter(prefix="/students/{student_id}/profile", tags=["user_profiles"])


@router.post("/", response_model=UserProfile, status_code=status.HTTP_201_CREATED)
def create_profile(student_id: int, data: UserProfileCreate, session: Session = Depends(get_session)):
    """Создание профиля студента"""
    if not crud.get_student_by_id(session, student_id):
        raise HTTPException(status_code=404, detail="Студент не найден")
    if crud.get_user_profile(session, student_id):
        raise HTTPException(status_code=400, detail="Профиль уже существует")
    return crud.create_user_profile(session, student_id, data)


@router.get("/", response_model=UserProfile)
def get_profile(student_id: int, session: Session = Depends(get_session)):
    """Получение профиля студента"""
    profile = crud.get_user_profile(session, student_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return profile


@router.put("/", response_model=UserProfile)
def update_profile(student_id: int, data: UserProfileUpdate, session: Session = Depends(get_session)):
    """Обновление профиля студента"""
    profile = crud.update_user_profile(session, student_id, data)
    if not profile:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return profile


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(student_id: int, session: Session = Depends(get_session)):
    """Удаление профиля студента"""
    if not crud.delete_user_profile(session, student_id):
        raise HTTPException(status_code=404, detail="Профиль не найден")
