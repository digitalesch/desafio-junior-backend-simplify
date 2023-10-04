from sqlalchemy import create_engine
import sqlalchemy.orm as orm
import os

PG_BACKEND_HOST = os.getenv("PG_BACKEND_HOST")
PG_BACKEND_PWD = os.getenv("PG_BACKEND_PWD")
PG_BACKEND_PORT = os.getenv("PG_BACKEND_PORT")

print(PG_BACKEND_PWD, PG_BACKEND_PORT)

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@db:5432/postgres"
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{PG_BACKEND_PWD}@{PG_BACKEND_HOST}:{PG_BACKEND_PORT}/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = orm.declarative_base()

# Dependency
def  get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
