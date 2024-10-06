class Runway:
    def __init__(self, name: str, length: float, heading: float, start_loc_x: float, start_loc_y: float, end_loc_x: float, end_loc_y: float, active: bool = True):
        self.name = name
        self.length = length
        self.heading = heading
        self.start_loc_x = start_loc_x
        self.start_loc_y = start_loc_y
        self.end_loc_x = end_loc_x
        self.end_loc_y = end_loc_y
        self.active = active