import pygame.image

####------ Screen ------####
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 30


####------ Main Page ------####
PERIODS_NAMES = {1: "Ancient Egypt",
                 2: "Ancient Rome",
                 3: "The medieval",
                 4: "Industrial Revolution",
                 5: "Modern Time"}


# The background image
HOMEPAGE_BACKGROUND_IMG = pygame.image.load("Assets\\Home_Page_Assets\\HOMEPAGE_BACKGROUND_IMG.png")


####------ Time Line animation ------####

# The length of the animation
TIME_AXIS_ANIMATION_LENGTH = 100

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
                 "Assets\\Time_Axis_Animation\\Periods_Icons\\gear.png",
                 "Assets\\Time_Axis_Animation\\Periods_Icons\\Nowdays.jpg"]

# The periods text
Y_POS_TIMELINE_TEXT = (WINDOW_HEIGHT//6)*5
Y_POS_TIMELINE_ICONS = Y_POS_TIMELINE_TEXT - PERIOD_ICON_HEIGHT * 0.35
X_POS_TEXTS_SCOPE = (0, WINDOW_WIDTH)

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


####------ Boss fight page ------####
QUESTION_RECT_X_POS = 0
QUESTION_RECT_Y_POS = WINDOW_HEIGHT // 2 + 20

BOSS_FIGHT_BACKGROUNDS_LIST = [
    "Assets\\Egypt\\egypt.jpeg",
    "Assets\\Medieval\\medieval.jpeg",
    "Assets\\Rome\\rome.jpeg",
    "Assets\\Industrial_Revolution\\industrial_revolution_background.jpeg",
    "Assets\\Modern_Time\\modern_time.jpeg"
]

BOSS_IMAGES_LIST = [
    ["Assets\\Enemies\\egypt_boss\\egypt_boss_1.png", "Assets\\Enemies\\egypt_boss\\egypt_boss_2.png"],
    ["Assets\\Enemies\\medieval_boss\\medieval_boss_1.png", "Assets\\Enemies\\medieval_boss\\medieval_boss_2.png"],
    ["Assets\\Enemies\\rome_boss\\rome_boss_1.png", "Assets\\Enemies\\rome_boss\\rome_boss_2.png"],
    ["Assets\\Enemies\\industrial_revolution_boss\\industrial_revolution_boss_1.png", "Assets\\Enemies\\industrial_revolution_boss\\industrial_revolution_boss_2.png"],
    ["Assets\\Enemies\\modern_time_boss\\modern_time_boss_1.png", "Assets\\Enemies\\modern_time_boss\\modern_time_boss_2.png"],
]

####------ Player ------####
PLAYER_X_POS = 300
PLAYER_Y_POS = WINDOW_HEIGHT * 0.84
PLAYER_HEALTH = 100
PLAYER_SPEED = 5
PLAYER_IMG_PATH = "Assets\\idle\\idle1.png"
PLAYER_IDLE_FRAMES = [
    pygame.image.load("Assets\\Player_Animations\\idle\\idle1.png"),
    pygame.image.load("Assets\\Player_Animations\\idle\\idle1.png"),
    pygame.image.load("Assets\\Player_Animations\\idle\\idle1.png"),
    pygame.image.load("Assets\\Player_Animations\\idle\\idle1.png")
]
PLAYER_ATTACK_FRAMES = [
    # pygame.image.load("Assets/Player_Animations/attack/attack1.png"),
    # pygame.image.load("Assets/Player_Animations/attack/attack2.png"),
    pygame.image.load("Assets/Player_Animations/attack/attack3.png")
    # pygame.image.load("Assets/Player_Animations/attack/attack4.png"),
    # pygame.image.load("Assets/Player_Animations/attack/attack5.png"),
    # pygame.image.load("Assets/Player_Animations/attack/attack6.png"),
    # pygame.image.load("Assets/Player_Animations/attack/attack7.png")
]
PLAYER_RUN_FRAMES = [
    pygame.image.load("Assets/Player_Animations/run/run1.png"),
    pygame.image.load("Assets/Player_Animations/run/run2.png"),
    pygame.image.load("Assets/Player_Animations/run/run3.png"),
    pygame.image.load("Assets/Player_Animations/run/run4.png"),
    pygame.image.load("Assets/Player_Animations/run/run5.png"),
    pygame.image.load("Assets/Player_Animations/run/run6.png"),
]


####------ Font ------####
FONT1 = "Fonts\\font_1.otf"
FONT2 = "Fonts\\font_2.ttf"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

####------ Musics ------####
HOMEPAGE_BACKGROUND_MUSIC = "Musics\\background_music1.mp3"

####------ Certificate ------####
CERTIFICATE_IMAGE = "Assets\\Certificate.png"