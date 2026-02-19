from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from ..database import get_session
from ..models import Category, CategoryCreate, CategoryUpdate
from .. import crud

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreate, session: Session = Depends(get_session)):
    """Создание новой категории"""
    return crud.create_category(session, data)


@router.get("/", response_model=List[Category])
def get_all_categories(session: Session = Depends(get_session)):
    """Список всех категорий"""
    return crud.get_all_categories(session)


@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, session: Session = Depends(get_session)):
    """Категория по ID"""
    category = crud.get_category_by_id(session, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category


@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, data: CategoryUpdate, session: Session = Depends(get_session)):
    """Обновление категории"""
    category = crud.update_category(session, category_id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, session: Session = Depends(get_session)):
    """Удаление категории (у студентов category_id станет NULL)"""
    if not crud.delete_category(session, category_id):
        raise HTTPException(status_code=404, detail="Категория не найдена")
