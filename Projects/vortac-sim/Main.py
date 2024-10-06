import tkinter as tk
import Draw_Utils as DU
import Aircraft
import Airport
import Runway
import Waypoint

WINDOW_WIDTH = 1200.0 # units in px
WINDOW_HEIGHT = 800.0 # units in px
AIRPORT_ICON_PADDING = 10.0 # units in px
AIRPORT_NAME_TEXT_SPACING_LEFT = 40.0 # units in px
RUNWAY_LENGTH_SCALAR = 0.010 # Adjust this value to scale the runway length.
WAYPOINT_ICON_RADIUS = 5.0 # units in px

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Vortac Sim: Air Traffic Control Radar')

        # Setting up the VORTAC canvas.
        self.canvas = tk.Canvas(self.root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = '#262626')
        self.canvas.pack()

        # Loading in the airplane-icon image.
        # self.airplane_icon = tk.PhotoImage(file = './icons8-plane-32.png')

        # Create a new Airport.
        airport = self.create_airport()
        # Draw the new Airport onto the VORTAC canvas.
        DU.Draw_Utils(self.canvas).draw_airport(airport)

        # Create respective runways.
        runway = self.create_runway(airport)
        # Draw the new Runway onto the VORTAC canvas.
        DU.Draw_Utils(self.canvas).draw_runway(runway)

        # Create a list of waypoints as (name, (x, y))
        waypoints = [('Alpha', (1000, 200)), ('Beta', (200, 200)), ('Charlie', (1000, 600)), ('Delta', (200, 600))]
        WAYPOINTS_LIST = []
        for waypoint in waypoints:
            new_waypoint = Waypoint.Waypoint(waypoint[0], waypoint[1][0], waypoint[1][1])
            WAYPOINTS_LIST.append(new_waypoint)
        # Draw each waypoint onto the VORTAC canvas.
        for waypoint in WAYPOINTS_LIST:
            DU.Draw_Utils(self.canvas).draw_waypoint(waypoint)
        
        aircraft = self.create_aircraft('SDM147', 'B789', 900.0, 450.0, 17000, 265, 360.0)
        DU.Draw_Utils(self.canvas).draw_aircraft(aircraft)

    def create_airport(self) -> Airport:
        name: str = 'NX77'
        loc_x: float = 600.0
        loc_y: float = 400.0
        number_of_runways: int = 1
        runways = ['36']
        airport = Airport.Airport(name, loc_x, loc_y, number_of_runways, runways)
        print('\nnew airport created!')
        return airport
    
    def create_runway(self, airport: Airport):
        # TODO: Implement this method to create a new runway based on the provided airport.
        name: str = '36'
        length: float = 10000.0
        heading:float = 360.0
        start_loc_x = 600
        start_loc_y = 400 + AIRPORT_ICON_PADDING
        end_loc_x = 600
        end_loc_y = 400 + AIRPORT_ICON_PADDING + (length * RUNWAY_LENGTH_SCALAR)
        active = True
        runway = Runway.Runway(name, length, heading, start_loc_x, start_loc_y, end_loc_x, end_loc_y, active)
        print('\nnew runway created!')
        return runway

    def create_waypoint(self, name: str, x_loc: float, y_loc: float, active: bool):
        waypoint = Waypoint.Waypoint(name, x_loc, y_loc, active)
        return waypoint
    
    def create_aircraft(self, flight_number: str, ac_type: str, x_loc: float, y_loc: float, altitude: float, speed: float, heading: float):
        aircraft = Aircraft.Aircraft(flight_number, ac_type, x_loc, y_loc, altitude, speed, heading)
        return aircraft

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    root.mainloop()