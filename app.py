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