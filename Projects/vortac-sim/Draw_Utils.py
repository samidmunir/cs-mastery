from Main import WINDOW_WIDTH, WINDOW_HEIGHT, AIRPORT_ICON_PADDING, AIRPORT_NAME_TEXT_SPACING_LEFT
import tkinter as tk
import Airport

class Draw_Utils:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw_airport(self, airport: Airport.Airport):
        print('\nhere')
        # Compute top-left coordinates for rectangle (airport)
        x1 = airport.loc_x - AIRPORT_ICON_PADDING
        y1 = airport.loc_y - AIRPORT_ICON_PADDING
        # Compute bottom-right coordinates rectangle (airport)
        x2 = airport.loc_x + AIRPORT_ICON_PADDING
        y2 = airport.loc_y + AIRPORT_ICON_PADDING
        
        # Draw a rectangle to represent an airport.
        self.canvas.create_rectangle(x1, y1, x2, y2, fill = '#ffffff')

        # Draw airport name
        self.canvas.create_text(airport.loc_x + AIRPORT_NAME_TEXT_SPACING_LEFT, airport.loc_y, text = airport.name, fill = '#ffffff', font = ('Arial', 12))