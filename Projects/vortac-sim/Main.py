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