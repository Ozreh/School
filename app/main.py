from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from .database import engine
from .routers import students
from .models import Student  # Импортируем модели для создания таблиц

# Создание таблиц в базе данных
SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Students API",
    description="API for managing students",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(students.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Students API",
        "docs": "/docs",
        "endpoints": [
            "POST /students/ - Create student",
            "GET /students/ - Get all students",
            "GET /students/{id} - Get student by ID",
            "PUT /students/{id} - Update student",
            "DELETE /students/{id} - Delete student"
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}