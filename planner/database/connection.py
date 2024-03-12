from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from planner.models.events import Event
from planner.models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pymongo import MongoClient



class Settings(BaseSettings):
    DATABASE_URL: str | None = 'mongodb://localhost:27017/planner'
    SECRET_KEY: str | None = 'HI5HL3V3L$3CR3T'

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[Event, User])



class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> list[any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> any:
        doc_id = id
        des_body = body.dict()

        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

