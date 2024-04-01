import sys
from player import *
from Pages_Manager import *
from Gif_Object import *

# Initialize Pygame
pygame.init()

# Set up the clock
clock = pygame.time.Clock()

# Creating Screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Time Travel -Voyage Through History')

# Creating the player
# the_player = player()

# gif_object(screen, 50, 50, 0, 0, 0, SAND_CLOCK_FRAMES).add_on_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PagesManager.time_line_page(screen, 1, 0)
    # Update the display and cap the frame rate
    pygame.display.flip()
    clock.tick(FPS)
