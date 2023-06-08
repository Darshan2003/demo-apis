from pydantic import BaseModel

class Login(BaseModel):
    phone: str = "917834811114"
    password: str = "secret1234"