class GameStateManager:
    """A class which manage the pages of the games"""

    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


# class PagesManager:
#     """A class which manage the gui pages of the game"""
#
#     @staticmethod
#     def time_line_page(screen, period_digit):
#         # The function get the game's screen and an integer which represent the period by these values:
#         # 1 - Ancient Egypt,
#         # 2 - The Medieval,
#         # 3 - The Ancient Rome,
#         # 4 - The Industrial Revolution,
#         # 5 - Modern Times.
#         # The function run the time-line animation.
#         if not 0 < period_digit <= len(TIME_LINE_PERIODS_LIST):
#             print("The period digit should be between 1 - 5")
#             return
#
#         x_pos_first_text = WINDOW_WIDTH * (1 / 4)
#         x_pos_third_text = WINDOW_WIDTH * (3 / 4)
#         x_pos_second_text = WINDOW_WIDTH
#
#         for i in range(len(SAND_CLOCK_FRAMES)):
#             # The background
#             image_object(screen, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0, 0, TIME_LINE_ANIMATION_BACKGROUND).add_on_screen()
#
#             # The timeline axis
#             image_object(screen, WINDOW_WIDTH, WINDOW_HEIGHT // 2, 0, (WINDOW_HEIGHT // 2), 0,
#                          TIME_LINE_AXIS_ARROW).add_on_screen()
#
#             # The timeline text
#             if x_pos_first_text >= WINDOW_WIDTH + 100:
#                 x_pos_first_text = (-100)
#
#             if x_pos_second_text >= WINDOW_WIDTH + 100:
#                 x_pos_second_text = (-100)
#
#             if x_pos_third_text >= WINDOW_WIDTH + 100:
#                 x_pos_third_text = (-100)
#
#             Game.add_text(screen, TIME_LINE_PERIODS_LIST[period_digit - 1], BLACK, x_pos_first_text, Y_POS_TIMELINE_TEXT, 25)
#             Game.add_text(screen, TIME_LINE_PERIODS_LIST[period_digit - 1], BLACK, x_pos_second_text, Y_POS_TIMELINE_TEXT, 25)
#             Game.add_text(screen, TIME_LINE_PERIODS_LIST[period_digit - 1], BLACK, x_pos_third_text, Y_POS_TIMELINE_TEXT, 25)
#
#             x_pos_first_text += 1
#             x_pos_second_text += 1
#             x_pos_third_text += 1
#
#             # The timeline's period icon
#             image_object(screen, PERIOD_ICON_HEIGHT, PERIOD_ICON_WIDTH, WINDOW_WIDTH * (1 / 2), (WINDOW_HEIGHT//6)*4.5 - PERIOD_ICON_HEIGHT * 0.35, 0, TIME_LINE_AXIS_ICONS[period_digit-1]).add_on_screen()
#
#             # The sand clock animation image
#             # The checking here is for the frame where the sand clock is horizontal and flip.
#             if i == 5:
#                 image_object(screen, SAND_CLOCK_SIZE, SAND_CLOCK_SIZE / 1.4, WINDOW_WIDTH // 2 - SAND_CLOCK_SIZE // 2,
#                              WINDOW_HEIGHT // 2 - SAND_CLOCK_SIZE // 2, 0, SAND_CLOCK_FRAMES[i]).add_on_screen()
#             else:
#                 image_object(screen, SAND_CLOCK_SIZE / 1.4, SAND_CLOCK_SIZE, WINDOW_WIDTH // 2 - SAND_CLOCK_SIZE // 2, WINDOW_HEIGHT // 2 - SAND_CLOCK_SIZE//2, 0, SAND_CLOCK_FRAMES[i]).add_on_screen()
#             pygame.display.flip()
#             pygame.time.wait(200)
