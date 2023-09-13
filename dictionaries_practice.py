my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)
vehicle = my_vehicle.copy()
vehicle["number_of_tires"] = 4
vehicle.pop("mileage")

for x in vehicle:
    print(x)
