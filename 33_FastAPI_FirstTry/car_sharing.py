from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import FileResponse
import os


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