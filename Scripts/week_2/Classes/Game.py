import pygame
import sys
from Classes.Pages_Manager import *
from Classes.Game_Pages import *
from constants import *

class Game:
    """ A class which manage the game."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('Home')
        self.home = HomePage(self.screen, self.gameStateManager)
        self.time_axis = TimeAxisPage(self.screen, self.gameStateManager)
        self.egypt = EgyptPage(self.screen, self.gameStateManager)

        self.states = {'Home': self.home, 'TimeAxis': self.time_axis, 'Egypt': self.egypt}

        pygame.display.set_caption('Time Travel -Voyage Through History')

    def run(self):

        self.states[self.gameStateManager.get_state()].prim_run()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)
