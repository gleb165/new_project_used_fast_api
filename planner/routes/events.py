from fastapi import APIRouter, HTTPException, status, Body
from planner.models.events import Event, EventUpdate
from beanie import PydanticObjectId
from planner.database.connection import Database

event_router = APIRouter(tags=["Event"])

event_database = Database(Event)


@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    events = await event_database.get_all()
    return events


@event_router.get('/{id}', response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event


@event_router.post("/")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully"
    }


@event_router.put('/{id}', response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event



@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> bool:
    event = await event_database.get(id)
    if event:
        return await event_database.delete(id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist")