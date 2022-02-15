from fastapi import FastAPI
from .database.database import database
from .api import router

app = FastAPI()
app.include_router(router)

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

