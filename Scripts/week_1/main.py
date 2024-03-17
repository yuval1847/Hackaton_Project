from constants import *
import sys
import pygame

# Initialize Pygame
pygame.init()

# Set up the clock
clock = pygame.time.Clock()

# Creating Screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Time Travel -Voyage Through History')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display and cap the frame rate
    pygame.display.flip()
    clock.tick(FPS)