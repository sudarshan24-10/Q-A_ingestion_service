# database/postgres.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repository.model.embedding_vector_model import Base
from config import Config

# Create engine once (Singleton via module load)
engine = create_engine(
    Config.DATABASE_URL,
    pool_pre_ping=True,
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def init_db():
    """
    Create tables (optional if using Supabase schema already)
    """
    Base.metadata.create_all(bind=engine)
    print("Database has been created")


def get_db():
    """
    FastAPI dependency.
    Provides a new session per request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()