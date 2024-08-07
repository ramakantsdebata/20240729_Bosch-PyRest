from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi import Depends
import os
import uvicorn

from contextlib import asynccontextmanager

from sqlmodel import create_engine
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import select

from .schema import Car
from .schema import CarInput
from .schema import Car_DBModel
from .schema import TripInput, Trip
from .schema import load_lib
from .schema import save_db
from .schema import Trip_DBModel


db = load_lib()


engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},
    echo=True
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    SQLModel.metadata.create_all(engine)

    # App execution
    yield

    # Shutdown code
    print("That's all folks!")

app = FastAPI(title="Car Sharing", lifespan=lifespan)


def get_session():
    '''
    This method will be passed as an optional dependency to methods using a session.
    Whenever those methods are invoked, this method is first invoked to get a session

    As this yields the session from within a context mgr block, and so the method
    calling get_session() receives a generator, effectively wrapping the caller inside
    the with-block. So, if an exception occurs, the session will be automatically rolled 
    back, protecting the operation from data corruption and lack of integrity.
    '''
    with Session(engine) as session:
        yield session


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    '''Serves the favicon.ico file'''
    return FileResponse(os.path.join('static', 'favicon.ico'))


# If we want to filter based on 'size' / 'doors' / both / None
@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None, session: Session = Depends(get_session)) -> list:
    query = select(Car_DBModel)
    if size is not None:
        query = query.where(Car_DBModel.size == size)
    if doors is not None:
        query = query.where (Car_DBModel.doors >= doors)
    
    return session.exec(query).all()


@app.get("/api/cars/{id}", response_model=Car)
def car_by_id(id: int, session: Session = Depends(get_session)) -> Car:
    car = session.get(Car_DBModel, id)
    if car:
        print(type(car))
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id = {id}.")


@app.post("/api/cars/", response_model=Car_DBModel)
def add_car(car: CarInput, session: Session = Depends(get_session)) -> Car_DBModel:
    new_car = Car_DBModel.model_validate(car)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car


@app.post("/api/cars/migrate")
def migrate_data_to_db(session: Session = Depends(get_session)) -> list[Car_DBModel]:
    for car in db:
        new_car = Car_DBModel.model_validate(car, update={'trips': []})
        session.add(new_car)
        session.commit()
        session.refresh(new_car)
        for trip in car.trips:
            new_trip = Trip_DBModel.model_validate(trip, update={'car_id': new_car.id, 'id': None})
            session.add(new_trip)
            session.commit()
            session.refresh(new_trip)

    return db


@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id: int, session: Session = Depends(get_session)) -> None:
    car = session.get(Car_DBModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@app.put("/api/cars/{id}", response_model=Car_DBModel)
def change_car(id: int, new_data: CarInput, session: Session = Depends(get_session)) -> Car_DBModel:
    car = session.get(Car_DBModel, id)
    if car:
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission

        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@app.post("/api/cars/{car_id}/trips", response_model=Trip_DBModel)
def add_trip(car_id: int, trip: TripInput, session: Session = Depends(get_session)) -> Trip_DBModel:
    car = session.get(Car_DBModel, car_id)
    if car:
        new_trip = Trip_DBModel.model_validate(trip, update={'car_id': car_id, 'id': None})
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id}")


if __name__ == '__main__':
    uvicorn.run("car_sharing:app", reload=True)
