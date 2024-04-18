import pygame

class Slider:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        self.value = 0.5  # Initial value (between 0 and 1)
        self.slide_button = None
        self.is_dragging = False  # Flag to indicate if slider is being dragged

    def draw(self, screen):
        # Draw track
        pygame.draw.rect(screen, (128, 128, 128), (self.x, self.y, self.length, 40))

        # Draw passed part
        passed_width = int(self.value * self.length)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y + 5, passed_width, 30))

        # Draw outline
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.length, 40), 8)

        # Draw handle
        handle_x = int(self.x + self.value * self.length)

        if (handle_x <= self.x + self.length - 10):
            self.slide_button = pygame.draw.rect(screen, (255, 255, 255), (handle_x, self.y, 10, 40), 40)


    def update_value(self, mouse_x):
        # Update value based on mouse position
        self.value = max(0, min(1, (mouse_x - self.x) / self.length))

    def checkForInput(self, position):
        if position[0] in range(self.slide_button.left - 5, self.slide_button.right + 5) and position[1] in range(self.slide_button.top + 5,
                                                                                          self.slide_button.bottom - 5):
            return True
        return False

    def get_value(self):
        return self.value