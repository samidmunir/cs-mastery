import random
import numpy as np

class Aircraft:
    def __init__(self, flight_number, waypoints):
        self.flight_number = flight_number
        self.speed = random.uniform(400, 600) # speed in knots
        self.altitude = random.uniform(30000, 40000) # altitude in feet
        self.position = np.array(waypoints[0]) # starting at first waypoint
        self.waypoints = waypoints
        self.current_waypoint = 1
        self.destination = np.array(waypoints[self.current_waypoint])
        self.heading = self.calculate_heading()

    def calculate_heading(self):
        # Calculate unit vector direction from current position to the next waypoint.
        direction = self.destination - self.position
        distance = np.linalg.norm(direction)
        if distance == 0:
            return np.zeros_like(direction)
        return direction / distance