class Waypoint:
    def __init__(self, name: str, x_loc: float, y_loc: float, acitve: bool = True):
        self.name = name
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.active = acitve