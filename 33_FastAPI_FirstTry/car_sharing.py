import os
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse
import uvicorn

from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from db import engine
from routers import cars
from routers import web
from routers import auth
from routers.cars import BadTripException

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    print("That's all folks!")


app = FastAPI(title="Car Sharing", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)
app.include_router(auth.router)


@app.exception_handler(BadTripException)
async def uvicorn_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad trip"},
    )


@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie", value="you_visited_the_carsharing_app")
    return response


# Now, after making any request to the service, 
# check out the cookie by inspecting browser 
# (F12 > Storage > Cookies > http://localhost:8000) 


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)
