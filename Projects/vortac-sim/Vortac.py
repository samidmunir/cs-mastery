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
        # TODO: function draw_runway()

if __name__ == '__main__':
    root = tk.Tk()
    app = Vortac(root)
    root.mainloop()