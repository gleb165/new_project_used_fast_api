from pydantic import BaseModel
from beanie import Document


class Event(Document):
    creator: str | None = None
    title: str
    image: str
    descriptions: str
    tags: list[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "descriptions": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: str | None = None
    image: str | None = None
    descriptions: str | None = None
    tags: list[str] | None = None
    location: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "descriptions": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }



