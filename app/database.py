from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

# Выбор базы данных (по умолчанию SQLite для разработки)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Для SQLite нужно добавить аргументы подключения
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session