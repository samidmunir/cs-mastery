"""
Setting up the GUI window (vortac screen)
- Tkinter library is used for creating GUI applications
"""

import tkinter as tk

# CONST VARIABLES
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# Initializing the main window.
class Vortac:
    def __init__(self, root):
        self.root = root
        self.root.title('Vortac Sim: Air Traffic Control Radar')

        # Seting up the canvas for the vortac.
        self.canvas = tk.Canvas(self.root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = '#262626')
        self.canvas.pack()

        # Call the function to draw the airport and runways.
        self.draw_airport()
    
    def draw_airport(self):
        # Placeholder: Draw a simple rectangle to represent the airport.
        self.canvas.create_rectangle(400, 400, 420, 420, fill = '#ffffff')

        # Draw the two runways with labels.
        self.draw_runway(410, 420, 410, 470, '36', '+')
        self.draw_runway(410, 400, 410, 350, '18', '-')


    def draw_runway(self, x1, y1, x2, y2, label, text_direction):
        # Draw a simple runway line.
        self.canvas.create_line(x1, y1, x2, y2, fill = '#00e100', width = 3)
        # Label the runway.
        if (text_direction == '+'):
            self.canvas.create_text(x1, y2 + 10, text = label, fill = 'white', font = ('Helvetica', 10))
        else:
            self.canvas.create_text(x1, y2 - 10, text = label, fill = 'white', font = ('Helvetica', 10))

if __name__ == '__main__':
    root = tk.Tk()
    app = Vortac(root)
    root.mainloop()