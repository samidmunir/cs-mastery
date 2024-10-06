from Main import AIRPORT_ICON_PADDING, AIRPORT_NAME_TEXT_SPACING_LEFT, WAYPOINT_ICON_RADIUS, AIRCRAFT_HEADING_VECTOR_LENGTH
import math
import Aircraft
import Airport
import Runway
import Waypoint

class Draw_Utils:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw_airport(self, airport: Airport.Airport):
        # Compute top-left coordinates for rectangle (airport)
        x1 = airport.loc_x - AIRPORT_ICON_PADDING
        y1 = airport.loc_y - AIRPORT_ICON_PADDING
        # Compute bottom-right coordinates rectangle (airport)
        x2 = airport.loc_x + AIRPORT_ICON_PADDING
        y2 = airport.loc_y + AIRPORT_ICON_PADDING
        
        # Draw a rectangle to represent an airport.
        self.canvas.create_rectangle(x1, y1, x2, y2, fill = '#ffffff')

        # Draw airport name
        self.canvas.create_text(airport.loc_x + AIRPORT_NAME_TEXT_SPACING_LEFT, airport.loc_y, text = airport.name, fill = '#ffffff', font = ('Helvetica', 12))
    
    def draw_runway(self, runway: Runway.Runway):
        self.canvas.create_line(runway.start_loc_x, runway.start_loc_y, runway.end_loc_x, runway.end_loc_y, fill = '#00e100', width = 3)
        self.canvas.create_text(runway.end_loc_x, (runway.end_loc_y + AIRPORT_ICON_PADDING), text = runway.name, fill = '#ffffff', font = ('Helvetica', 12))

    def draw_waypoint(self, waypoint: Waypoint.Waypoint):
        self.canvas.create_oval(waypoint.x_loc - WAYPOINT_ICON_RADIUS, waypoint.y_loc - WAYPOINT_ICON_RADIUS, waypoint.x_loc + WAYPOINT_ICON_RADIUS, waypoint.y_loc + WAYPOINT_ICON_RADIUS, fill = '#ffffff' if waypoint.active else '#e10000')
        self.canvas.create_text(waypoint.x_loc + AIRPORT_NAME_TEXT_SPACING_LEFT, waypoint.y_loc, text = waypoint.name, fill = '#ffffff', font = ('Helvetica', 12))

    def draw_aircraft(self, aircraft: Aircraft.Aircraft):
        # self.canvas.create_image(aircraft.x_loc, aircraft.y_loc, image = self.airplane_icon, anchor = tk.CENTER)
        points = [(aircraft.x_loc, aircraft.y_loc - 10), (aircraft.x_loc - 5, aircraft.y_loc + 5), (aircraft.x_loc + 5, aircraft.y_loc + 5)]
        # print(f'\naircraft.x_loc: {aircraft.x_loc}, aircraft.y_loc: {aircraft.y_loc}')
        # print('points:', points)

        angle_rad = math.radians(aircraft.heading)

        rotated_points = []
        for px, py in points:
            new_x, new_y = self.rotate_points(px, py, aircraft.x_loc, aircraft.y_loc, angle_rad)
            rotated_points.append((new_x, new_y))

        self.canvas.create_polygon(rotated_points, fill = '#0000ff', outline = '#ffffff', width = 1.5)
        
        info = f'{aircraft.flight_number} {aircraft.ac_type}\n{aircraft.speed}kts {aircraft.altitude}ft\n{aircraft.heading}°'
        
        self.canvas.create_text(aircraft.x_loc + 60, aircraft.y_loc - 20, text = info, fill = '#ffffff', font = ('Helvetica', 10))
        # self.draw_aircraft_heading_vector(aircraft)
    
    def draw_aircraft_heading_vector(self, aircraft: Aircraft.Aircraft):
        a = aircraft.x_loc + AIRCRAFT_HEADING_VECTOR_LENGTH * math.cos(math.radians(aircraft.heading + 90.0))
        b = aircraft.y_loc - AIRCRAFT_HEADING_VECTOR_LENGTH * math.sin(math.radians(aircraft.heading + 90.0))

        # self.canvas.create_line(aircraft.x_loc, aircraft.y_loc, aircraft.x_loc, aircraft.y_loc - AIRCRAFT_HEADING_VECTOR_LENGTH, fill = '#ffffff', width = 1.5)
        self.canvas.create_line(aircraft.x_loc, aircraft.y_loc, a, b, fill = '#ffffff', width = 1.5)
    
    def rotate_points(self, x, y, cx, cy, angle_rad):
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        x -= cx
        y -= cy

        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta

        x_rotated = x_new + cx
        y_rotated = y_new + cy

        return x_rotated, y_rotated

    def draw_terrain_polygon(self, points):
        self.canvas.create_polygon(points, fill = '#04e100', outline = '#ff0000', width = 1.5)