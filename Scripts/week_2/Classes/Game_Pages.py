import pygame.sprite
import sys
from Classes.Game import *
from Classes.Image_Object import *
from constants import *
from Classes.AnimatedSprite import *
from Classes.Button import *

class HomePage:
    """A class of the home page."""

    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def prim_run(self):
        pygame.mixer.music.load(HOMEPAGE_BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1)

    def run(self):
        # The function get nothing
        # The function run all the elements of this page

        # The background
        self.display.blit(HOMEPAGE_BACKGROUND_IMG, (0, 0))

        # A tuple of (x, y) which indicate the mouse position
        menu_mouse_pos = pygame.mouse.get_pos()

        # The main title
        menu_text = pygame.font.Font(FONT2, 25).render("Time Travel - Voyage Through History", True, "#2a9d8f")
        menu_rect = menu_text.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.display.blit(menu_text, menu_rect)

        # The buttons
        player_button = Button(None, pos=(WINDOW_WIDTH // 2, 300), text_input="PLAY", font=pygame.font.Font(FONT2, 20), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(None, pos=(WINDOW_WIDTH // 2, 350), text_input="OPTIONS", font=pygame.font.Font(FONT2, 20), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(None, pos=(WINDOW_WIDTH // 2, 400), text_input="QUIT", font=pygame.font.Font(FONT2, 20), base_color="#d7fcd4", hovering_color="White")

        # Changing the font color while holding on the button
        for button in [player_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(self.display)

        # Checking for mouse click on the buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_button.checkForInput(menu_mouse_pos):
                    self.gameStateManager.set_state("TimeAxis")
                if options_button.checkForInput(menu_mouse_pos):
                    pass
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pass

class TimeAxisPage:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # The sand clock animation
        self.sandClockAnimation = AnimatedSprite(SAND_CLOCK_FRAMES, SAND_CLOCK_ANIMATION_DURATION, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    def prim_run(self):
        pass

    def run(self):
        # The function get nothing
        # The function run all the elements of this page

        # The background
        image_object(self.display, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0, 0, TIME_LINE_ANIMATION_BACKGROUND).add_on_screen()

        # The TimeAxis
        image_object(self.display, TIME_LINE_WIDTH, TIME_LINE_HEIGHT, TIME_LINE_POS_X, TINE_LINE_POS_Y, 0, TIME_LINE_AXIS_ARROW).add_on_screen()

        # Update and blit the sand clock animation on the screen
        self.sandClockAnimation.update()
        self.display.blit(self.sandClockAnimation.image, self.sandClockAnimation.rect)


class EgyptPage:
    """A class of the egypt period."""

    def prim_run(self):
        pass

    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        # The function get nothing
        # The function run all the elements of this page
        pass