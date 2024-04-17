import pygame
from constants import *

class MovingTextAnimation:
    """A class which represent a moving text and image"""

    def __init__(self, text, start_position, x_scope, periodNumber):

        pygame.init()

        # Creating the text itself
        self.font = pygame.font.Font(FONT2, 40)
        self.text_surface = self.font.render(text, True, (0, 0, 0))

        # The position of the text
        self.text_x, self.text_y = start_position
        self.x_scope = x_scope

        # Load image
        print(PERIODS_ICONS[periodNumber-1])
        # self.image = pygame.image.load(PERIODS_ICONS[periodNumber-1])
        # self.image = pygame.transform.scale(self.image, (75, 60))  # Scale the image if necessary

        self.last_time = pygame.time.get_ticks()

    def run(self, screen):

        # Draw text
        screen.blit(self.text_surface, (self.text_x, self.text_y))

        # Draw image
        # image_x = self.text_x + self.text_surface.get_width() + 10  # Adjust the position as necessary
        # image_y = self.text_y + self.text_surface.get_height() // 2 - 30  # Adjust the position as necessary
        # screen.blit(self.image, (image_x, image_y))

        # Update animation state
        current_time = pygame.time.get_ticks()
        dt = (current_time - self.last_time) / 1000.0
        self.last_time = current_time
        self.text_x += 100 * dt

        if self.text_x > self.x_scope[1]:
            self.text_x = self.x_scope[0] - self.text_surface.get_width()