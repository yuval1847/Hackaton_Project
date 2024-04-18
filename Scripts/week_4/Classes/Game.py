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
        self.home = HomePage(self.screen, self.gameStateManager, self.clock)
        self.time_axis = TimeAxisPage(self.screen, self.gameStateManager, 1, self.clock)
        self.finalBossPage = finalBossPage(self.screen, self.gameStateManager, self.clock)
        self.certificatePage = CertificatePage(self.screen, self.gameStateManager)
        self.settingsPage = Settings(self.screen, self.gameStateManager)
        self.states = {'Home': self.home,
                       'TimeAxis': self.time_axis,
                       'finalBoss': self.finalBossPage,
                       'Certificate': self.certificatePage,
                       'Settings': self.settingsPage}

        pygame.display.set_caption('Time Travel - Voyage Through History')

    def run(self):
        self.states[self.gameStateManager.get_state()].prim_run()
        while True:
            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)