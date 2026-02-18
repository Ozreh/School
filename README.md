# School API

FastAPI + SQLModel + SQLite

## Запуск

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Документация: http://127.0.0.1:8000/docs

## Структура

```
app/
├── main.py        # Точка входа FastAPI
├── database.py    # SQLite engine + сессия
├── models.py      # SQLModel модели (students, user_profiles)
├── crud.py        # CRUD функции
└── routers/
    ├── students.py
    └── user_profiles.py
```

## Эндпоинты

### Students
| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/students/` | Создать студента |
| GET | `/students/` | Все студенты |
| GET | `/students/{id}` | Студент по ID |
| PUT | `/students/{id}` | Обновить студента |
| DELETE | `/students/{id}` | Удалить студента |

### User Profiles
| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/students/{id}/profile` | Создать профиль |
| GET | `/students/{id}/profile` | Получить профиль |
| PUT | `/students/{id}/profile` | Обновить профиль |
| DELETE | `/students/{id}/profile` | Удалить профиль |

> При удалении студента его профиль удаляется автоматически (CASCADE).
