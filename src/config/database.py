# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
# pyrefly: ignore [missing-import]
from sqlalchemy.ext.declarative import declarative_base
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos (SQLite por defecto)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Para MySQL usarías algo como:
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@post/db_name"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependencia para obtener la sesión de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
