from sqlmodel import create_engine, Session
from sqlalchemy import event
from sqlalchemy.engine import Engine

DATABASE_URL = "sqlite:///./school.db"

# Включаем поддержку внешних ключей в SQLite (по умолчанию выключена!)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
