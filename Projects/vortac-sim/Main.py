import pygame
import numpy as np
from simulation import initialize_aircraft, update_airspace
from waypoints import get_waypoints

# Initialize pygame module
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('AI Airspace Simulation')
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Function to draw aircraft on screen.
def draw_aircraft(screen, aircraft):
    # Draw the aircraft as a blue circle.
    pygame.draw.circle(screen, BLUE, aircraft.position.astype(int), 10)
    # Draw flight info
    text = font.render(aircraft.display_info(), True, WHITE)
    screen.blit(text, aircraft.position.astype(int) + np.array([10, -20]))

def run_simulation(aircraft_count):
    # Initialize aircraft
    aircrafts = initialize_aircraft(aircraft_count)

    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        (screen.fill((0, 0, 0)))

        # Update airspace
        time_step = clock.get_time() / 1000 # Time step in seconds
        update_airspace(aircrafts, time_step)

        # Draw all aircrafts
        for aircraft in aircrafts:
            draw_aircraft(screen, aircraft)

        # Update the display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(60)

    pygame.quit()

# Run the simulation
if __name__ == '__main__':
    run_simulation(3)