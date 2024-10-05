"""
Setting up the GUI window (vortac screen)
- Tkinter library is used for creating GUI applications
"""

import tkinter as tk

# Initializing the main window.
class Vortac:
    def __init__(self, root):
        self.root = root
        self.root.title('Vortac Sim: Air Traffic Control Radar')

        # Seting up the canvas for the vortac.
        self.canvas = tk.Canvas(self.root, width = 800, height = 600, bg = 'black')
        self.canvas.pack()

        # Call the function to draw the airport and runways.
        # TODO: function draw_airport()
    
    def draw_runway(self, x1, y1, x2, y2, label):
        # Draw a simple runway line.
        self.canvas.create_line(x1, y1, x2, y2, fill = 'white', width = 3)
        # Label the runway.
        self.canvas.create_text(x1, y1 - 10, text = label, fill = 'white', font = ('Helvetica', 10))

if __name__ == '__main__':
    root = tk.Tk()
    app = Vortac(root)
    root.mainloop()