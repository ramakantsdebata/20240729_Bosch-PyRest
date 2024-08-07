from pydantic import BaseModel
import json

class CarInput(BaseModel):
    size: str
    fuel: str
    doors: int
    transmission: str


class Car(CarInput):
    id: int


fileName = "cars.json"
def load_lib() -> list[Car]:
    with open(fileName, "r") as file:
        cars = json.load(file)
    
    # ret_val = [Car.model_validate(car) for car in cars]
    ret_val = []
    for dt in cars:
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
