from constants import *
from Classes.Image_Object import *
from Classes.Bar import *

class Boss:
    """A class which represent a boss in the game"""

    def __init__(self, display, periodNumber):
        self.display = display
        self.health = 120
        self.periodNumber = periodNumber
        self.gotHit = 0 # 0 - not got hit, 1 - got hit
        self.xPos = PLAYER_X_POS + 300
        self.yPos = PLAYER_Y_POS - 120
        self.healthBar = LifeBar(x=self.xPos+50, y=self.yPos, width=100, height=10, max_life=self.health)

    def run(self):
        image_object(screen=self.display, width=160, length=160, x_pos=self.xPos, y_pos=self.yPos, tag_id=0, image_path=BOSS_IMAGES_LIST[self.periodNumber][self.gotHit]).add_on_screen()

        # Check if the boss got heart
        if self.gotHit == 1:
            pygame.time.wait(10)
            self.gotHit = 0
            self.health -= 20
            self.healthBar.update_life(self.health)

            # Check if the boss is dead
            if self.health <= 0:
                self.periodNumber += 1
                self.health = 120
                self.healthBar = LifeBar(x=self.xPos+50, y=self.yPos, width=100, height=10, max_life=self.health)

        # The life bar of the boss rendering
        self.healthBar.add_on_screen(self.display)