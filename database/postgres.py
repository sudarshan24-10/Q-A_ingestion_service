import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repository.model.embedding_vector_model import Base
from config import Config


class PostgresDB:

    def __init__(self):
        self.database_url = Config.DATABASE_URL

        self.engine = create_engine(
            self.database_url,
            pool_pre_ping=True,
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )

    def init_db(self):
        """
        Initialize tables (optional if already created in Supabase)
        """
        Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        """
        Create new DB session (Unit of Work)
        """
        return self.SessionLocal()
