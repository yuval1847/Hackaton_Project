from Classes.Image_Object import *
from Animations import *

class PagesManager:
    """A class which manage the gui pages of the game"""

    @staticmethod
    def time_line_page(screen, period_digit, sand_clock_index):
        # The function get the game's screen and an integer which represent the period by these values:
        # 1 - Ancient Egypt,
        # 2 - The Medieval,
        # 3 - The Ancient Rome,
        # 4 - The Industrial Revolution,
        # 5 - Modern Times.
        # The function run the time-line animation.

        for i in range(len(SAND_CLOCK_FRAMES)):
            # The background
            image_object(screen, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0, 0, TIME_LINE_ANIMATION_BACKGROUND).add_on_screen()

            # The timeline axis
            image_object(screen, WINDOW_WIDTH, WINDOW_HEIGHT // 2, 0, (WINDOW_HEIGHT // 2), 0,
                         TIME_LINE_AXIS_ARROW).add_on_screen()

            # The sand clock animation image
            # The checking here is for the frame where the sand clock is horizontal and flip.
            if i == 5:
                image_object(screen, SAND_CLOCK_SIZE, SAND_CLOCK_SIZE / 1.4, WINDOW_WIDTH // 2 - SAND_CLOCK_SIZE // 2,
                             WINDOW_HEIGHT // 2 - SAND_CLOCK_SIZE // 2, 0, SAND_CLOCK_FRAMES[i]).add_on_screen()
            else:
                image_object(screen, SAND_CLOCK_SIZE / 1.4, SAND_CLOCK_SIZE, WINDOW_WIDTH // 2 - SAND_CLOCK_SIZE // 2, WINDOW_HEIGHT // 2 - SAND_CLOCK_SIZE//2, 0, SAND_CLOCK_FRAMES[i]).add_on_screen()

            pygame.display.flip()
            pygame.time.wait(200)
