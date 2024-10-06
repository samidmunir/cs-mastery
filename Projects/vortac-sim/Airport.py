class Airport:
    def __init__(self, name: str, loc_x: float, loc_y: float, number_of_runways: int, runways: list):
        self.name = name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.number_of_runways = number_of_runways
        self.runways = runways