import pygame
from constants import *
from Image_Object import *
from Rect_Object import *
class player:
    """A class which represent a player in the game"""

    def __init__(self, player_image_path):
        self.image_path = image_object(player_image_path, )
        self.rect = rect_object()
        self.speed = PLAYER_SPEED
        self.health = PLAYER_HEALTH

    def add_on_screen(self):
        # The function get nothing.
        # The function add the enemy's rectangle on the screen and above it the player's image.
        # self.the_rect.add_on_screen()
        self.the_image.add_on_screen()

    def update(self, keys):
        # The function get the key which the user entered
        # The function update the player's movement according to the key

        # Enter w (up)
        if keys[pygame.K_w]:
            self.rect.y -= self.speed

        # Enter s (down)
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        # Enter a (left)
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        # Enter d (right)
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Put the player on the screen
