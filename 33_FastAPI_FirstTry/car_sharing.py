from fastapi import FastAPI
from fastapi import HTTPException
from datetime import datetime
from fastapi.responses import FileResponse
import os
import uvicorn
from .schema import load_lib

db = load_lib()


app = FastAPI()


@app.get("/")
def welcome():
    """Return a friendly welcome message to visitors"""
    return {"message": "Welcome to Car Sharing App"}


@app.get("/date")
def date():
    """Return a friendly welcome message to visitors"""
    return {"date": datetime.now()}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Serves the icon file"""
    return FileResponse(os.path.join("static", "favicon.ico"))

@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None) -> list:
    result = db
    if size is not None:
        result = [car for car in result if car.size == size]
    if doors is not None:
        result = [car for car in result if car.doors == doors]
    return result

@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)