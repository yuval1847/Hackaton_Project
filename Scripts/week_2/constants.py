import pygame.image

####------ Screen ------####
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 30


####------ Main Page ------####

# The background image
HOMEPAGE_BACKGROUND_IMG = pygame.image.load("Assets\\Home_Page_Assets\\HOMEPAGE_BACKGROUND_IMG.png")


####------ Time Line animation ------####

# The background image
TIME_LINE_ANIMATION_BACKGROUND = "Assets\\Time_Axis_Animation\\Space_Background.png"

# The timeline axis
TIME_LINE_WIDTH = WINDOW_WIDTH
TIME_LINE_HEIGHT = WINDOW_HEIGHT // 2.5
TIME_LINE_POS_X = 0
TINE_LINE_POS_Y = WINDOW_HEIGHT * (2 / 3)
TIME_LINE_AXIS_ARROW = "Assets\\Time_Axis_Animation\\Time_Axis_Arrow.png"

# The periods icons
PERIOD_ICON_WIDTH = 50
PERIOD_ICON_HEIGHT = PERIOD_ICON_WIDTH * 1.5
PERIODS_ICONS = ["Assets\\Time_Axis_Animation\\Periods_Icons\\egypt_icon.jpg",
                        "Assets\\Time_Axis_Animation\\Periods_Icons\\rome_icon.jpg",
                        "Assets\\Time_Axis_Animation\\Periods_Icons\\medival_icon.jpg",
                        "Assets\\Time_Axis_Animation\\Periods_Icons\\industrial_revolution.jpg",
                        "Assets\\Time_Axis_Animation\\Periods_Icons\\Nowdays.jpg"]

# The periods text
Y_POS_TIMELINE_TEXT = (WINDOW_HEIGHT//6)*4.5
Y_POS_TIMELINE_ICONS = Y_POS_TIMELINE_TEXT - PERIOD_ICON_HEIGHT * 0.35

# The sand clock
SAND_CLOCK_SIZE = 80
SAND_CLOCK_ANIMATION_DURATION = 5
SAND_CLOCK_FRAMES = [pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_1.png"),
                     pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_2.png"),
                     pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_3.png"),
                     pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_4.png"),
                     pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_5.png"),
                     pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_6.png"),
                     pygame.image.load("Assets\\Time_Axis_Animation\\Sand_clock_ticking\\sand_clock_7.png")]
SAND_CLOCK_FRAMES = [pygame.transform.scale(frame, (SAND_CLOCK_SIZE, SAND_CLOCK_SIZE)) for frame in SAND_CLOCK_FRAMES]


####------ Player ------####
PLAYER_HEALTH = 100
PLAYER_SPEED = 5
PLAYER_IMG_PATH = "Assets\\idle\\idle1.png"

####------ Font ------####
FONT1 = "Fonts\\font_1.otf"
FONT2 = "Fonts\\font_2.ttf"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

####------ Musics ------####
HOMEPAGE_BACKGROUND_MUSIC = "Musics\\background_music1.mp3"
