from pydantic import BaseModel

class Login(BaseModel):
    phone: str
    password: str