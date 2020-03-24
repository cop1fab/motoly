import datetime
from datetime import date
from .db import db


class Driver(db.Document):
    motorcycle = db.BooleanField(default=True)
    name = db.StringField(required=True)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)

