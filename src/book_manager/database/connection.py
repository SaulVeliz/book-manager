import os

from dotenv import load_dotenv

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from book_manager.models.models import Base

load_dotenv()


class ConexionDB:

    def __init__(self):

        host = os.getenv(
            "SUPABASE_HOST"
        )

        database = os.getenv(
            "SUPABASE_DB"
        )

        user = os.getenv(
            "SUPABASE_USER"
        )

        password = os.getenv(
            "SUPABASE_PASSWORD"
        )

        db_url = (
            f"postgresql+psycopg2://"
            f"{user}:{password}"
            f"@{host}:5432/{database}"
        )

        self.engine = create_engine(
            db_url,
            echo=False
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )

    def crear_tablas(self):

        Base.metadata.create_all(
            self.engine
        )

    def obtener_sesion(self):

        return self.SessionLocal()

    @contextmanager
    def get_session(self):

        session = self.SessionLocal()

        try:

            yield session

            session.commit()

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()