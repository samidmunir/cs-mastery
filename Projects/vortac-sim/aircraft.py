class Aircraft:
    def __init__(self, flight_number: str, ac_type: str, x_loc: float, y_loc: float, altitude: float, speed: float, heading: float):
        self.flight_number = flight_number
        self.ac_type = ac_type
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.altitude = altitude
        self.speed = speed
        self.heading = heading

        # Plan data structure to control the aircraft.
        self.plan = None

        # Current step in the plan
        self.current_step = 0
        self.time_in_current_step = 0
    
    def assign_plan(self, plan):
        self.plan = plan
        self.current_step = 0
        self.time_in_current_step = 0
    
    def update_position(self, delta_time):
        if not self.plan or self.current_step >= len(self.plan):
            return # No plan or we are done with the steps.
        
        step = self.plan[self.current_step]
        t = min(self.time_in_current_step / step['duration'], 1.0)

        # Interpolating between current position and target position.
        self.x_loc = (1 - t) * self.x_loc + t * step['target_x']
        self.y_loc = (1 - t) * self.y_loc + t * step['target_y']
        self.altitude = (1 - t) * self.altitude + t * step['altitude']
        self.heading = step['heading'] # Updating the heading directly

        # Update the time spent in this step.
        self.time_in_current_step += delta_time
        if self.time_in_current_step >= step['duration']:
            self.current_step += 1
            self.time_in_current_step = 0