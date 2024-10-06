import tkinter as tk

WINDOW_WIDTH = 1200 # units in px
WINDOW_HEIGHT = 800 # units in px

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Vortac Sim: Air Traffic Control Radar')

        # Setting up the VORTAC canvas.
        self.canvas = tk.Canvas(self.root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = '#262626')
        self.canvas.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    root.mainloop()