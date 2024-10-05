import pygame
from simulation import initialize_aircraft, update_airspace
from waypoints import get_waypoints

# Initialize pygame module
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('AI Airspace Simulation')
font = pygame.font.Font(None, 36)