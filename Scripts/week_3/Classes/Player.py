from constants import *
from Classes.Image_Object import *
from Classes.AnimatedSprite import *


class Player:
    """A class which represent a player"""

    def __init__(self):
        self.player_attack_animation = AnimatedSprite(PLAYER_ATTACK_FRAMES, 5, (PLAYER_X_POS, PLAYER_Y_POS))
        self.player_idle_animation = AnimatedSprite(PLAYER_IDLE_FRAMES, 5, (PLAYER_X_POS, PLAYER_Y_POS))
        self.current_animation = self.player_idle_animation

#     def run(self):
