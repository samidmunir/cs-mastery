class Aircraft:
    def __init__(self, flight_number: str, ac_type: str, x_loc: float, y_loc: float, altitude: float, speed: float, heading: float):
        self.flight_number = flight_number
        self.ac_type = ac_type
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.altitude = altitude
        self.speed = speed
        self.heading = heading