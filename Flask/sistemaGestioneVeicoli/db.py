from car import Car
from van import Van
from fleetManager import FleetManager

c1: Car = Car("BG123AE", "Nissan Micra", "Lorenzo Rossi", 1997, "maintenance", 3, False)
v1: Van = Van("PR234BJ", "Mercedes", "Alessandro Popa", 2007, "rented", 200, False)

rental: FleetManager = FleetManager()
rental.add(c1)
rental.add(v1)


