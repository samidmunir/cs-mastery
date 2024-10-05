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
    
    def update_position(self, time_step):
        # Move the aircraft in the direction of its heading
        distance_travelled = self.speed * time_step / 3600  # Distance in nautical miles
        movement = self.heading * distance_travelled

        # Ensure movement is a NumPy array
        movement = np.array(movement)

        # Ensure self.position and movement are compatible types
        self.position = self.position.astype(float)  # Convert to float type for precision
        self.position += movement

        # Check if the aircraft has reached the next waypoint
        if np.linalg.norm(self.destination - self.position) < 1:  # Close enough
            self.current_waypoint += 1
            if self.current_waypoint < len(self.waypoints):
                self.destination = np.array(self.waypoints[self.current_waypoint])
                self.heading = self.calculate_heading()
    
    def display_info(self):
        return f'Flight: {self.flight_number} | Altitude: {self.altitude:.0f} ft| Speed: {self.speed:.0f} kts'