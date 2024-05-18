from fastapi import FastAPI

from database import engine
from models import Base

from auth.routers import router as authRouter
app=FastAPI()
app.include_router(authRouter,prefix='/auth')

Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return {"msg":"welcome to my home page!!"}
