import tkinter as tk
import Draw_Utils as DU
import time
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
AIRCRAFT_HEADING_VECTOR_LENGTH = 40.0 # units in px

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

        self.WAYPOINTS_LIST = WAYPOINTS_LIST

        # Create a list of aircrafts as (name, ac_type, x_loc, y_loc, altitude, speed, heading)
        aircrafts = [
            ('SDM147', 'B789', 900.0, 450.0, 17000, 265, 360.0),
            # ('UAL225', 'B38M', 320.0, 325.0, 15000, 250, 180.0),
            # ('DAL1738', 'A20N', 250.0, 300.0, 21000, 300, 135.0),
            # ('SYMA5', 'A380', 925.0, 185.0, 5000, 275, 270.0)
        ]
        AIRCRAFTS_LIST = []
        for aircraft in aircrafts:
            new_aircraft = Aircraft.Aircraft(aircraft[0], aircraft[1], aircraft[2], aircraft[3], aircraft[4], aircraft[5], aircraft[6])
            AIRCRAFTS_LIST.append(new_aircraft)
        # Draw each aircraft onto the VORTAC canvas.
        for aircraft in AIRCRAFTS_LIST:
            DU.Draw_Utils(self.canvas).draw_aircraft(aircraft)
        
        # aircraft = self.create_aircraft('SDM147', 'B789', 900.0, 450.0, 17000, 265, 360.0)
        # DU.Draw_Utils(self.canvas).draw_aircraft(aircraft)

        # Create points for terrain regions on VORTAC canvas.
        # terrain_1_points = [(100, 100), (200, 200), (300, 100)]
        # terrain_2_points = [(500, 300), (600, 400), (400, 400)]
        # terrain_3_points = [(700, 500), (800, 600), (600, 600)]
        # DU.Draw_Utils(self.canvas).draw_terrain_polygon(terrain_1_points)
        # DU.Draw_Utils(self.canvas).draw_terrain_polygon(terrain_2_points)
        # DU.Draw_Utils(self.canvas).draw_terrain_polygon(terrain_3_points)

        # Assign a plan to the aircraft
        plan = [
            {'target_x': 1000, 'target_y': 200, 'speed': 300, 'altitude': 25000, 'heading': 360, 'duration': 5000},
            {'target_x': 200, 'target_y': 200, 'speed': 315, 'altitude': 25000, 'heading': 360, 'duration': 5000},
            {'target_x': 1000, 'target_y': 600, 'speed': 300, 'altitude': 25000, 'heading': 3600, 'duration': 5000},
        ]
        AIRCRAFTS_LIST[0].assign_plan(plan)
        # AIRCRAFTS_LIST[1].assign_plan(plan)

        # Start time
        self.start_time = time.time()
        self.AIRCRAFTS_LIST = AIRCRAFTS_LIST

        # Start the animation
        self.animate()

    def create_airport(self) -> Airport:
        name: str = 'NX77'
        loc_x: float = 600.0
        loc_y: float = 400.0
        number_of_runways: int = 1
        runways = ['36']
        airport = Airport.Airport(name, loc_x, loc_y, number_of_runways, runways)
        # print('\nnew airport created!')
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
        # print('\nnew runway created!')
        return runway

    def create_waypoint(self, name: str, x_loc: float, y_loc: float, active: bool):
        waypoint = Waypoint.Waypoint(name, x_loc, y_loc, active)
        return waypoint
    
    def create_aircraft(self, flight_number: str, ac_type: str, x_loc: float, y_loc: float, altitude: float, speed: float, heading: float):
        aircraft = Aircraft.Aircraft(flight_number, ac_type, x_loc, y_loc, altitude, speed, heading)
        return aircraft
    
    def animate(self):
        # # Calculate delta time
        # current_time = time.time()
        # delta_time = current_time - self.start_time
        # self.start_time = current_time

        # # Update the aircraft positions based on their plans.
        # for aircraft in self.AIRCRAFTS_LIST:
        #     aircraft.update_position(delta_time)

        #     # Draw the updated aircraft on the VORTAC canvas.
        #     DU.Draw_Utils(self.canvas).draw_aircraft(aircraft)
        # self.canvas.update()
        # # Repeat the animation at 60fps
        # self.root.after(int(1000 / 60), self.animate)

        # Calculate delta time
        current_time = time.time()
        delta_time = current_time - self.start_time
        self.start_time = current_time

        # Clear the entire canvas to refresh it
        self.canvas.delete("all")

        # Redraw static elements (airport, runways, waypoints)
        airport = self.create_airport()
        DU.Draw_Utils(self.canvas).draw_airport(airport)

        runway = self.create_runway(airport)
        DU.Draw_Utils(self.canvas).draw_runway(runway)

        for waypoint in self.WAYPOINTS_LIST:
            DU.Draw_Utils(self.canvas).draw_waypoint(waypoint)

        # Update the aircraft positions based on their plans.
        for aircraft in self.AIRCRAFTS_LIST:
            aircraft.update_position(delta_time)

            # Draw the updated aircraft on the VORTAC canvas
            DU.Draw_Utils(self.canvas).draw_aircraft(aircraft)

        # Repeat the animation at 60fps
        self.root.after(int(1000 / 60), self.animate)


if __name__ == '__main__':
    # Create the tkinter window.
    root = tk.Tk()
    app = Main(root)
    # Run the tkinter main loop.
    root.mainloop()