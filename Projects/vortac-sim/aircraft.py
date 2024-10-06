class Aircraft:
    def __init__(self, flight_number: str, ac_type: str, altitude: float, speed: float, heading: float):
        self.flight_number = flight_number
        self.ac_type = ac_type
        self.altitude = altitude
        self.speed = speed
        self.heading = heading