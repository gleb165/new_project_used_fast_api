from pydantic import BaseModel, EmailStr
from planner.models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "event": "[list Event]",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }