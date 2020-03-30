import json
from datetime import date

from flask import Flask, jsonify, request, make_response

from database.db import initialize_db
from database.models import Driver, Battery, Station, Vehicle, Swap, Odometer

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
    vehicle_obj = request.get_json()
    vehicle = Vehicle(odometer_reading=vehicle_obj["odometer_reading"]).save()
    return make_response(jsonify({"message": "successfully created vehicle",
                                  "vehicle": json.loads(vehicle.to_json())})), 201


@app.route("/swap/driver/<driver_id>/battery/<battery_id>/station/<station_id>", methods=["POST"])
def create_swap(driver_id, battery_id, station_id):
    swap = request.get_json()
    Swap(remainingBattery=swap["initialBattery"],
         initialBattery=swap["initialBattery"],
         driver=driver_id,
         battery=battery_id,
         station=station_id
         ).save()
    return make_response(jsonify(swap)), 201


@app.route("/swap/<swap_id>", methods=["PUT"])
def make_swap(swap_id):
    swap = request.get_json()
    Swap.objects.get(id=swap_id).update(remainingBattery=swap["remainingBattery"], swapped=True)
    return make_response(jsonify({"message": "successfully made swap"})), 200


@app.route("/swap/driver/<driver_id>/vehicle/<vehicle_id>/day", methods=["POST"])
def get_used_energy(driver_id, vehicle_id):
    reading_got = request.get_json()
    swaps = Swap.objects(driver=driver_id, swapped=True, timestamp=date.today()).to_json()
    reading = Vehicle.objects(id=vehicle_id, timestamp=date.today())
    data = json.loads(swaps)
    total_initial_power = 0
    total_remaining_power = 0
    for i in data:
        if i["initialBattery"]:
            total_initial_power += i["initialBattery"]
        if i["remainingBattery"]:
            total_remaining_power += i["remainingBattery"]
    total_power_used = total_initial_power - total_remaining_power
    Odometer(vehicle=vehicle_id, current_reading=reading_got["reading"]).save()
    return make_response(jsonify({"power_used": total_power_used,
                                  "kilometers": json.loads(reading.to_json())})), 200


@app.route("/vehicle/<vehicle_id>/day", methods=["GET"])
def get_kilometers_done(vehicle_id):
    reading = Odometer.objects(vehicle=vehicle_id, timestamp=date.today()).to_json()
    reading_data = json.loads(reading)
    km_done = 0
    for i in reading_data:
        km_done += i["current_reading"]-i["previous_reading"]
    return make_response(jsonify({"kilometers": km_done})), 200


@app.route("/swap/driver/<driver_id>", methods=["GET"])
def get_swaps_made_by_driver(driver_id):
    swaps = Swap.objects(driver=driver_id).to_json()
    return make_response(swaps), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
