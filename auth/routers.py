from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from models import Users
from database import SessionLocal
from sqlalchemy.orm import session
from .schemas import RegisterReq,LoginReq
router=APIRouter()

oauth_schema=OAuth2PasswordBearer(tokenUrl='/auth/token')

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

@router.post('/token')
def getToken(form_data:OAuth2PasswordRequestForm=Depends(),db:session=Depends(get_db)):
    user=db.query(Users).filter(Users.uname==form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid User')
    elif not (user.password==form_data.password):
        raise HTTPException(status_code=404,detail='Invalid Credentials')
    else:
        return {'access_token':form_data.username+"::"+user.email}


@router.get('/current_user')
def get_current_user(token:str=Depends(oauth_schema)):
    print(token)
    return {'user':token.split("::")[0],'email':token.split("::")[1]}


@router.get("/users")
def allUsers(db:session=Depends(get_db)):
    return db.query(Users.id,Users.uname,Users.email).all()

@router.post('/register',status_code=status.HTTP_201_CREATED)
def register(registerReq:RegisterReq,db:session=Depends(get_db)):
    try:
        new_user=Users()
        new_user.uname=registerReq.username
        new_user.password=registerReq.password
        new_user.email=registerReq.email
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Couldn't register")

@router.post('/login',status_code=200)
def login(loginReq:LoginReq,db:session=Depends(get_db)):
    user=db.query(Users).filter(Users.uname==loginReq.username, Users.password==loginReq.password).first()
    if user:
        return {'msg':f"Login success.",'uname':user.uname}
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail='Invalid Credentials!!')
