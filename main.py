
from fastapi import FastAPI
from pydantic import BaseModel
from database import add_ride as save_ride, get_rides as get_saved_rides
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()


# creates a blueprint for one ride.
class Ride(BaseModel):
    trail: str
    miles: float
    minutes: int


# homepage
@app.get("/")
def home():
    return FileResponse("static/index.html")


# show all rides saved in the database
@app.get("/rides")
def get_rides():
    return get_saved_rides()


# creates a new ride
@app.post("/rides")
def add_ride(ride: Ride):
    save_ride(ride.trail, ride.miles, ride.minutes)
    return {
        "message": "Ride added successfully!",
        "ride": ride
    }
app.mount("/static", StaticFiles(directory="static"), name="static")
