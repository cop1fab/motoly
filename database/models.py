import datetime
from datetime import date
from .db import db


class Vehicle(db.Document):
    name = db.StringField(required=True, default="Honda")
    odometer_reading = db.FloatField(required=True, default=0.00)
    timestamp = db.DateTimeField(default=date.today())


class Odometer(db.Document):
    vehicle = db.ReferenceField(Vehicle, required=True, unique=True)
    current_reading = db.FloatField(required=True)
    previous_reading = db.FloatField(required=True, default=0.00)
    timestamp = db.DateTimeField(default=date.today())


class Driver(db.Document):
    name = db.StringField(required=True)
    vehicle = db.ReferenceField(Vehicle, required=True, unique=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)


class Battery(db.Document):
    voltage = db.FloatField(required=True)
    capacity = db.IntField(required=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)


class Station(db.Document):
    location = db.StringField(required=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)


class Swap(db.Document):
    swapped = db.BooleanField(default=False)
    remainingBattery = db.IntField(required=True)
    initialBattery = db.IntField(required=True)
    battery = db.ReferenceField(Battery, required=True)
    driver = db.ReferenceField(Driver, required=True)
    station = db.ReferenceField(Station, required=True)
    timestamp = db.DateTimeField(default=date.today())
