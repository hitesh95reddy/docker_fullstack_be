from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB_URI='sqlite:///./test.db'
DB_URI='postgresql://postgres:postgres@mydb:5432/postgres'
engine=create_engine(DB_URI)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
