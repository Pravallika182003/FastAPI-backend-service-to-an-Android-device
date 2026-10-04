from sqlalchemy import  create_engine  #python __ bridge to connect to the database
from sqlalchemy.orm import  sessionmaker ,  declarative_base  # to create a session and base class for models  

from app.config import settings
connect_args   =  {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)
SessionsLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def  get_db():
    db = SessionsLocal()
    try:
        yield db
    finally:
        db.close()