from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import FileResponse
import os


db = [
    {"id": 1, "size": "s", "fuel": "petrol",    "doors": 3, "transmission": "auto"  },
    {"id": 2, "size": "s", "fuel": "electric",  "doors": 3, "transmission": "auto"  },
    {"id": 3, "size": "s", "fuel": "petrol",    "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric",  "doors": 3, "transmission": "auto"  },
    {"id": 5, "size": "m", "fuel": "hybrid",    "doors": 5, "transmission": "auto"  },
    {"id": 6, "size": "m", "fuel": "petrol",    "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "disel",     "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric",  "doors": 5, "transmission": "auto"  },
    {"id": 9, "size": "l", "fuel": "hybrid",    "doors": 5, "transmission": "auto"  },
]



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
def favicon():
    """Serves the icon file"""
    return FileResponse(os.path.join("static", "favicon.ico"))

@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None):
    result = db
    if size is not None:
        result = [car for car in result if car['size'] == size]
    if doors is not None:
        result = [car for car in result if car['doors'] == doors]
    return result