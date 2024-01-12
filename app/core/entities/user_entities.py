from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    _id: Optional[str] = None
    username: str
    first_name: str
    last_name: str
    email: str
    password: str

    @classmethod
    def create(cls, username: str, first_name: str, last_name: str, email: str, password: str, _id: Optional[str] = None):
        return cls(
            _id=_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )