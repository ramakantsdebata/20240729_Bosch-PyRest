from sqlmodel import SQLModel, Field
from sqlmodel import Relationship
import json


class TripInput(SQLModel):
    start: int
    end: int
    description: str


class Trip_DBModel(TripInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    car_id: int = Field(foreign_key="car_dbmodel.id")
    car: "Car_DBModel" = Relationship(back_populates="trips")


class Trip(TripInput):
    id: int


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

class Car_DBModel(CarInput, table=True):
    id: int|None = Field(primary_key=True, default=None)
    trips: list[Trip_DBModel] = Relationship(back_populates="car")


class Car(CarInput):
    id: int
    trips: list[Trip] = []


fileName = "cars.json"
def load_lib() -> list[Car]:
    with open(fileName, "r") as file:
        lstDtCars = json.load(file)
    
    # ret_val = [Car.model_validate(car) for car in cars]
    ret_val = []
    for dt in lstDtCars:
        car_obj = Car.model_validate(dt)
        ret_val.append(car_obj)
    return ret_val


def save_db(list_of_cars: list[Car]):
    # json.dump(db, open(fileName, "w"))
    with open(fileName, "w") as file:
        # json.dump([car.model_dump() for car in list_of_cars], file, indent=4)
        lstDtCar = []
        for obj in list_of_cars:
            dt = obj.model_dump()
            lstDtCar.append(dt)
        json.dump(lstDtCar, file, indent=4)

if __name__ == "__main__":
    c1 = Car(id=1, size="m", fuel="petrol", doors=4, transmission="auto")
    print(c1)
    print(c1.dict())                # Deprecated
    print(c1.model_dump())          # Dumps object in a dict format

    print(c1.json())                # Deprecated
    print(c1.model_dump_json())     # Dumps the object in JSON format
