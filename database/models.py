import datetime
from datetime import date
from .db import db


class Vehicle(db.Document):
    odometer_reading = db.FloatField(required=True, default=0.00)
    timestamp = db.DateTimeField(default=date.today())


class Driver(db.Document):
    driver_name = db.StringField(required=True)
    vehicle = db.ReferenceField(Vehicle, required=True, unique=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)


class Battery(db.Document):
    voltage = db.FloatField(required=True)
    capacity = db.IntField(required=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)


class Station(db.Document):
    location = db.StringField(required=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)


