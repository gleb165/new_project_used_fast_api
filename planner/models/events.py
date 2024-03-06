from pydantic import BaseModel


class Event(BaseModel):
    id: int
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

