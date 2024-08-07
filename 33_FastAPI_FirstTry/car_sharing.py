from fastapi import FastAPI
from fastapi import HTTPException
from datetime import datetime
from fastapi.responses import FileResponse
import os
import uvicorn
from .schema import load_lib
from .schema import save_db
from .schema import Car
from .schema import CarInput
from .schema import TripInput, Trip


'''
GET - Fetch/Read
POST - Add/Write
PUT - UPdate an existing object
DELETE - Delete an object
'''


db = load_lib()


app = FastAPI(title="Bosch Training")


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
def get_cars(size: str|None = None, doors: int|None = None) -> list[Car]:
    result = db
    if size is not None:
        result = [car for car in result if car.size == size]
    if doors is not None:
        result = [car for car in result if car.doors == doors]
    return result

@app.get("/api/cars/{id}")
def car_by_id(id: int) -> Car:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


@app.post("/api/cars")
def add_car(carIn: CarInput):
    car = Car(size=carIn.size,
              fuel=carIn.fuel,
              doors=carIn.doors,
              transmission=carIn.transmission,
              id=len(db)+1)
    db.append(car)
    save_db(db)
    return car


@app.put("/api/cars/{id}", response_model=Car)
def update_car(id: int, new_car: CarInput) -> Car:
    result = [car for car in db if car.id == id]

    if result:
        car = result[0]
        car.size = new_car.size
        car.fuel = new_car.fuel
        car.doors = new_car.doors
        car.transmission = new_car.transmission
        save_db(db)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


@app.delete("/api/cars/{id}", status_code=204)
def delete_car(id: int):
    result = [car for car in db if car.id == id]
    if result:
        car = result[0]
        db.remove(car)
        save_db(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}")


@app.post("/api/cars/{car_id}/trips", response_model=Trip)
def add_trip(car_id: int, trip: TripInput) -> Trip:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        new_trip = Trip(id = len(car.trips) + 1,
                        start = trip.start, end = trip.end,
                        description = trip.description)
        car.trips.append(new_trip)
        save_db(db)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id}")


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)