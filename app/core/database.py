#establish engine , session and dependency 
from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker, Session
from collections.abc import Generator
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False, 
    bind=engine,
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
