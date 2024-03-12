from pydantic import EmailStr, BaseModel
from planner.models.events import Event
from beanie import Document


class User(Document):
    email: EmailStr
    password: str
    events: list[Event] | None = None

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "event": "[list Event]",
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
