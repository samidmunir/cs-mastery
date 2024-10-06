import tkinter as tk

# Plan: list of tuples with (x_change, y_change, duration in frames)
# Duration in frames, with 60fps, 60 frames = 1 second
plan = [
    (5, 0, 60),   # Move right 5 units for 1 second
    (0, 5, 60),   # Move down 5 units for 1 second
    (-5, 0, 60),  # Move left 5 units for 1 second
    (0, -5, 60)   # Move up 5 units for 1 second
]

class MovingSquareApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        # Create a square (rectangle)
        self.square = self.canvas.create_rectangle(190, 190, 210, 210, fill="blue")

        # Track the position of the square
        self.x_pos = 190
        self.y_pos = 190

        # Plan index and counters
        self.plan_index = 0
        self.plan_frame_count = 0
        self.current_plan = plan[0]

        # Start the animation
        self.animate()

    def animate(self):
        # Ensure the plan index does not go out of bounds
        if self.plan_index < len(plan):
            # Get the current step in the plan
            x_change, y_change, duration = self.current_plan

            # Update the position
            self.x_pos += x_change / duration
            self.y_pos += y_change / duration

            # Move the square on the canvas
            self.canvas.coords(self.square, self.x_pos, self.y_pos, self.x_pos + 20, self.y_pos + 20)

            # Increment the frame counter
            self.plan_frame_count += 1

            # If the frame count exceeds the duration, move to the next plan step
            if self.plan_frame_count >= duration:
                self.plan_frame_count = 0
                self.plan_index += 1
                if self.plan_index < len(plan):
                    self.current_plan = plan[self.plan_index]

        # Call the animate method again after 16ms (~60fps)
        self.root.after(16, self.animate)

# Create the Tkinter window
root = tk.Tk()
app = MovingSquareApp(root)

# Run the Tkinter main loop
root.mainloop()