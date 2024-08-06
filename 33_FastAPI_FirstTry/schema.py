from pydantic import BaseModel


class Car(BaseModel):
    id: int
    size: str
    fuel: str
    doors: int
    transmission: str


if __name__ == "__main__":
    c1 = Car(id=1, size="m", fuel="petrol", doors=4, transmission="auto")
    print(c1)
    print(c1.dict())                # Deprecated
    print(c1.model_dump())          # Dumps object in a dict format

    print(c1.json())                # Deprecated
    print(c1.model_dump_json())     # Dumps the object in JSON format
