from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
SERVER_DB = os.getenv("SERVER_DB")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")

DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@{SERVER_DB}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()