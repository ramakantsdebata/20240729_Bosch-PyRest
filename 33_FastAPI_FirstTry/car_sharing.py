import os
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse
import uvicorn

from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .db import engine
from .routers import cars
from .routers import web
from .routers.cars import BadTripException

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    print("That's all folks!")


app = FastAPI(title="Car Sharing", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)


@app.exception_handler(BadTripException)
async def uvicorn_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad trip"},
    )


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)
