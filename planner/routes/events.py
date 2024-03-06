from fastapi import APIRouter, HTTPException, status, Body
from planner.models.events import Event

event_router = APIRouter(tags=["Event"])

events = list()


@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    return events


@event_router.get('/{id}', response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/")
async def create_event(body: Event) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully"
    }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist")