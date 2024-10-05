import random
from aircraft import Aircraft
from waypoints import waypoints

def initialize_aircraft(aircraft_count):
    aircrafts = []
    for i in range(aircraft_count):
        flight_number = f'VN{random.randint(100, 999)}'
        route = random.sample(waypoints, len(waypoints)) # random route through waypoints.
        aircraft = Aircraft(flight_number, route)
        aircrafts.append(aircraft)
    return aircrafts

def update_airspace(aircrafts, time_step):
    for aircraft in aircrafts:
        aircraft.update_position(time_step)