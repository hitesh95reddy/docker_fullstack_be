from pydantic import BaseModel

class LoginReq(BaseModel):
    username: str
    password: str

class RegisterReq(BaseModel):
    username: str
    password: str
    email: str
