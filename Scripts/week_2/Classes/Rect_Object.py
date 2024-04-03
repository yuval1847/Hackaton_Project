import pygame

class rect_object(pygame.sprite.Sprite):
    """
    A class which represent a basic rectangle object

    The class attributes are:
    * length and width of the object: length, width: int
    * x and y position of the object: x_pos, y_pos: int
    * type of object(static objects, player, enemy): tag_id: int
      The possible values of the id is: 0 - static objects, 1 - player, 2 - enemy
    * color of the rectangle: color: tuple(RGB)
    """

    def __init__(self, screen, width, length, x_pos, y_pos, tag_id, color, is_solid):
        self.screen = screen
        self.length = length
        self.width = width
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tag_id = tag_id
        self.color = color
        self.is_solid = is_solid

    def get_rectangle(self):
        # The function get nothing
        # The function return the rectangle object (which is the official class of rectangle of pygame) of this rect_object
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.length)

    def add_on_screen(self):
        # The function get nothing
        # The function add the rectangle on the screen
        pygame.draw.rect(self.screen, self.color, (self.x_pos, self.y_pos, self.width, self.length))