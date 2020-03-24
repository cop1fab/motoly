import json
from flask import Flask, jsonify, request, make_response
from database.db import initialize_db
from database.models import Driver, Battery, Station, Vehicle


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/motors'
}
initialize_db(app)


@app.route("/", methods=['GET'])
def home():
    return "Welcome to motoly, your #1 app to manage electric vehicle business in Rwanda"


@app.route("/driver/<vehicle_id>", methods=["POST"])
def create_driver(vehicle_id):
    driver = request.get_json()
    new_driver = Driver(name=driver["name"], vehicle=vehicle_id).save()
    return make_response(jsonify({"driver": json.loads(new_driver.to_json())})), 201


@app.route("/drivers", methods=["GET"])
def get_drivers():
    drivers = Driver.objects().to_json()
    return make_response(drivers), 200


@app.route("/driver/driver_id", methods=["GET"])
def get_one_drivers():
    one_driver = Driver.objects().to_json()
    return make_response(one_driver), 200


@app.route("/battery", methods=["POST"])
def create_battery():
    battery = request.get_json()
    Battery(**battery).save()
    return make_response(jsonify(battery)), 201


@app.route("/batteries", methods=["GET"])
def get_batteries():
    batteries = Battery.objects().to_json()
    return make_response(batteries), 200


@app.route("/station", methods=["POST"])
def create_station():
    station = request.get_json()
    Station(location=station["location"]).save()
    return make_response(jsonify(station)), 201


@app.route("/stations", methods=["GET"])
def get_stations():
    stations = Station.objects().to_json()
    return make_response(stations), 200


@app.route("/vehicle", methods=["POST"])
def create_vehicle():
    vehicle = Vehicle().save()
    return make_response(jsonify({"message": "successfully created vehicle",
                                  "vehicle": json.loads(vehicle.to_json())})), 201


if __name__ == '__main__':
    app.run(port=5000, debug=True)
