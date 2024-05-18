from database import Base
from sqlalchemy import Column,String,Integer

class Users(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    uname=Column(String,unique=True)
    password=Column(String)
    email=Column(String,unique=True)
