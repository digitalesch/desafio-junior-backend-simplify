from sqlalchemy import create_engine
import sqlalchemy.orm as orm

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@db:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@localhost:5000/postgres"

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
