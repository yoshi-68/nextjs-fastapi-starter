from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

database_uri = "postgresql://postgres:postgres@localhost:5432/app"

# Engine の作成
engine = create_engine(database_uri, echo=True)

# 実際の DB セッション
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()


def get_db():  # type: ignore
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
