from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from planner.routes.users import user_router
from planner.routes.events import event_router
from planner.database.connection import Settings


import uvicorn

app = FastAPI()
s = Settings()


@app.on_event("startup")
async def init_db():
    await s.initialize_database()

# Register routes

app.include_router(user_router,  prefix="/user")
app.include_router(event_router, prefix="/event")



@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


