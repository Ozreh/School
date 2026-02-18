from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from .database import engine
from .models import Student, UserProfile  # Импорт обеих моделей для создания таблиц
from .routers import students, user_profiles

# Создание таблиц при старте
SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="School API",
    description="API для управления студентами и их профилями",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)
app.include_router(user_profiles.router)


@app.get("/", tags=["root"])
def root():
    return {
        "message": "School API работает!",
        "docs": "/docs",
        "endpoints": {
            "students": [
                "POST   /students/",
                "GET    /students/",
                "GET    /students/{id}",
                "PUT    /students/{id}",
                "DELETE /students/{id}",
            ],
            "user_profiles": [
                "POST   /students/{id}/profile",
                "GET    /students/{id}/profile",
                "PUT    /students/{id}/profile",
                "DELETE /students/{id}/profile",
            ],
        },
    }


@app.get("/health", tags=["root"])
def health():
    return {"status": "healthy"}
