from Main import AIRPORT_ICON_PADDING, AIRPORT_NAME_TEXT_SPACING_LEFT, WAYPOINT_ICON_RADIUS
import tkinter as tk
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