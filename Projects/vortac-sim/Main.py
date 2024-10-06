import tkinter as tk
import Draw_Utils as DU
import Airport

WINDOW_WIDTH = 1200.0 # units in px
WINDOW_HEIGHT = 800.0 # units in px
AIRPORT_ICON_PADDING = 10.0 # units in px
AIRPORT_NAME_TEXT_SPACING_LEFT = 40.0 # units in px

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Vortac Sim: Air Traffic Control Radar')

        # Setting up the VORTAC canvas.
        self.canvas = tk.Canvas(self.root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = '#262626')
        self.canvas.pack()

        # Create a new Airport.
        airport = self.create_airport()
        # Draw the new Airport onto the VORTAC canvas.
        # TODO: Use Draw_Utils to draw the airport.
        DU.Draw_Utils(self.canvas).draw_airport(airport)

        # draw_util = du.Draw_Utils(self.canvas)
        # draw_util.draw_airport(self, 'N51', 600.0, 400.0, 2, '18')
    
    def create_airport(self) -> Airport:
        name: str = 'NX77'
        loc_x: float = 600.0
        loc_y: float = 400.0
        number_of_runways: int = 1
        runways = ['18']
        airport = Airport.Airport(name, loc_x, loc_y, number_of_runways, runways)
        print('\nnew airport created!')
        return airport

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    root.mainloop()