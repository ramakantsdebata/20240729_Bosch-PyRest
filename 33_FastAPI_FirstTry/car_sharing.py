import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .db import engine
from .routers import cars
from .routers import web

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    print("That's all folks!")

app = FastAPI(title="Car Sharing", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)
