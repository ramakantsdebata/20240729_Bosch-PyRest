import os
from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter
from sqlmodel import Session
from sqlmodel import select
from fastapi.responses import FileResponse

from db import get_session

from schema import load_lib
from schema import save_db

from schema import Car
from schema import CarInput
from schema import Car_DBModel
from schema import TripInput, Trip
from schema import Trip_DBModel
from schema import User_DBModel

from routers.auth import get_current_user


db = load_lib()

router = APIRouter(prefix="/api/cars")

@router.get("/")
def get_cars(size: str|None = None, doors: int|None = None, session: Session = Depends(get_session)) -> list[Car]:
    query = select(Car_DBModel)
    if size is not None:
        query = query.where(Car_DBModel.size == size)
    if doors is not None:
        query = query.where (Car_DBModel.doors >= doors)
    
    return session.exec(query).all()


@router.get("/{id}", response_model=Car)
def car_by_id(id: int, session: Session = Depends(get_session)) -> Car:
    car = session.get(Car_DBModel, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id = {id}.")


@router.post("/", response_model=Car_DBModel)
def add_car(car: CarInput, session: Session = Depends(get_session),
            user: User_DBModel = Depends(get_current_user)) -> Car_DBModel:
    new_car = Car_DBModel.model_validate(car)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car


@router.post("/migrate")
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


@router.delete("/api/cars/{id}", status_code=204)
def remove_car(id: int, session: Session = Depends(get_session)) -> None:
    car = session.get(Car_DBModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.put("/api/cars/{id}", response_model=Car_DBModel)
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


class BadTripException(Exception):  # Custom Exception Class
    pass


@router.post("/api/cars/{car_id}/trips", response_model=Trip_DBModel)
def add_trip(car_id: int, trip: TripInput, session: Session = Depends(get_session)) -> Trip_DBModel:
    car = session.get(Car_DBModel, car_id)
    if car:
        new_trip = Trip_DBModel.model_validate(trip, update={'car_id': car_id, 'id': None})
        if new_trip.end < new_trip.start:
            raise BadTripException("Trip end before start")
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={car_id}")

