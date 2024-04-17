from constants import *
from Classes.Image_Object import *

class Boss:
    """A class which represent a boss in the game"""

    def __init__(self, display, periodNumber):
        self.display = display
        self.health = 120
        self.periodNumber = periodNumber
        self.gotHit = 0 # 0 - not got hit, 1 - got hit
        self.xPos = PLAYER_X_POS + 300
        self.yPos = PLAYER_Y_POS - 120

    def run(self):
        image_object(screen=self.display, width=160, length=160, x_pos=self.xPos, y_pos=self.yPos, tag_id=0, image_path=BOSS_IMAGES_LIST[self.periodNumber][self.gotHit]).add_on_screen()

        # Check if the boss got heart
        if self.gotHit == 1:
            pygame.time.wait(10)
            self.gotHit = 0
            self.health -= 20

            # Check if the boss is dead
            if self.health <= 0:
                self.periodNumber += 1
                self.health = 120

            print(self.health)