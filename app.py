from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


def average_temp(devices):
    """Return the average temperature of all devices."""
    total = sum(d["temp"] for d in devices)
    return total / len(devices)


def hottest(devices):
    """Return the dictionary of the device with the highest temperature."""
    return max(devices, key=lambda d: d["temp"])



@app.get("/devices")
def get_devices():
    return readings



@app.get("/devices/hottest")
def get_hottest_device():
    return hottest(readings)



@app.get("/devices/online")
def get_online_devices():
    return [device for device in readings if device["online"]]



@app.get("/devices/{name}")
def get_device(name: str):
    for device in readings:
        if device["name"] == name:
            return device
    raise HTTPException(status_code=404, detail=f"No device called {name}")




@app.get("/stats")
def get_stats():
    return {"average_temperature": round(average_temp(readings), 2)}



@app.post("/devices", status_code=201)
def create_device(device: dict):
    readings.append(device)
    return device



@app.get("/rooms/{room}/devices")
def get_devices_in_room(room: str):
    room_devices = [device for device in readings if device["room"] == room]
    if not room_devices:
        raise HTTPException(status_code=404, detail=f"No room called {room}")
    return room_devices