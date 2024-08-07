import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .db import engine
from .routers import cars


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    print("That's all folks!")

app = FastAPI(title="Car Sharing", lifespan=lifespan)
app.include_router(cars.router)
# app.include_router(bikes.router)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    '''Serves the favicon.ico file'''
    return FileResponse(os.path.join('static', 'favicon.ico'))


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)
