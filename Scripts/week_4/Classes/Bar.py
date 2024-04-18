import pygame
from constants import *

class LifeBar:
    def __init__(self, x, y, width, height, max_life):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_life = max_life
        self.current_life = max_life
        self.outline_color = (0, 0, 0)  # Black color for the outline
        self.heart_icon = pygame.image.load(HEART_ICON).convert_alpha()
        self.heart_icon = pygame.transform.scale(self.heart_icon, (20, 20))  # Resize the heart icon to match the height of the life bar

    def update_life(self, new_life):
        self.current_life = new_life

    def add_on_screen(self, screen):
        # Draw the outline of the life bar
        pygame.draw.rect(screen, self.outline_color, (self.x, self.y, self.width, self.height), 2)

        # Calculate the width of the life bar based on the current life
        life_bar_width = (self.current_life / self.max_life) * self.width

        # Calculate the color based on the current life percentage (linear interpolation from green to red)
        green = min(255, int(255 * (self.current_life / self.max_life)))
        red = min(255, int(255 * (1 - (self.current_life / self.max_life))))
        bar_color = (red, green, 0)

        # Draw the filled portion of the life bar
        pygame.draw.rect(screen, bar_color, (self.x, self.y, life_bar_width, self.height))

        # Draw the heart icon
        screen.blit(self.heart_icon, (self.x - self.height, self.y - (HEART_SIZE // 4)))
