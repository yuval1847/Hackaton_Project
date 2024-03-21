import pygame

class image_object(pygame.sprite.Sprite):
    """
    A class which represent a basic image object

    The class attributes are:
    * length and width of the object: length, width: int
    * x and y position of the object: x_pos, y_pos: int
    * type of object(static objects, player, enemy): tag_id: int
      The possible values of the id is: 0 - static objects, 1 - player, 2 - enemy
    * image path of the object: image_path: string
    * angle of rotation: angle: int
    """
    def __init__(self, screen, width, length, x_pos, y_pos, tag_id, image_path):
        self.screen = screen
        self.length = length
        self.width = width
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tag_id = tag_id
        self.image_path = image_path
        self.angle = 0

    def add_on_screen(self):
        # The function get nothing
        # The function add the object's image on the screen
        object_img = pygame.image.load(self.image_path)
        object_img = pygame.transform.scale(object_img, (self.width, self.length))
        object_img = pygame.transform.rotate(object_img, self.angle)
        self.screen.blit(object_img, (self.x_pos, self.y_pos))