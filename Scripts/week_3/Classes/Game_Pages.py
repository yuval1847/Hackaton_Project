import pygame.sprite
import sys
from Classes.Game import *
from Classes.Image_Object import *
from constants import *
from Classes.AnimatedSprite import *
from Classes.Button import *
from Classes.MovingTextAnimation import *
from Classes.Question import *
from Classes.Boss import *

class HomePage:
    """A class of the home page."""

    def __init__(self, display, gameStateManager, clock):
        self.display = display
        self.gameStateManager = gameStateManager
        self.clock = clock

    def prim_run(self):
        # pygame.mixer.music.load(HOMEPAGE_BACKGROUND_MUSIC)
        # pygame.mixer.music.play(-1)
        pass

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
    def __init__(self, display, gameStateManager, nextPeriodNumber, clock):
        self.display = display
        self.gameStateManager = gameStateManager
        self.nextPeriodNumber = nextPeriodNumber
        self.clock = clock
        self.start_time = pygame.time.get_ticks()  # Get the initial time
        self.animation_duration = 5000  # Duration of the animation in milliseconds
        self.show_warning = False  # Flag to indicate whether to show the warning text
        self.seconds_remaining = 5  # Total seconds for the countdown

        # The sand clock animation
        self.sandClockAnimation = AnimatedSprite(SAND_CLOCK_FRAMES, SAND_CLOCK_ANIMATION_DURATION, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        # The moving texts animation
        self.textAnimation = MovingTextAnimation(PERIODS_NAMES[self.nextPeriodNumber], (0, Y_POS_TIMELINE_TEXT), X_POS_TEXTS_SCOPE, self.nextPeriodNumber)

    def prim_run(self):
        pass

    def run(self):
        # The function get nothing
        # The function run all the elements of this page

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time

        # Calculate progress as a value between 0 and 1
        progress = min(elapsed_time / self.animation_duration, 1.0)

        # Calculate remaining seconds
        remaining_seconds = max(self.seconds_remaining - int(elapsed_time / 1000), 0)

        # Clear the screen
        self.display.fill(BLACK)

        # Draw background and other elements
        image_object(self.display, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0, 0, TIME_LINE_ANIMATION_BACKGROUND).add_on_screen()
        image_object(self.display, TIME_LINE_WIDTH, TIME_LINE_HEIGHT, TIME_LINE_POS_X, TINE_LINE_POS_Y, 0,
                     TIME_LINE_AXIS_ARROW).add_on_screen()

        # Update and blit the sand clock animation on the screen
        self.sandClockAnimation.update()
        self.display.blit(self.sandClockAnimation.image, self.sandClockAnimation.rect)

        # Update and blit the moving text animation
        self.textAnimation.run(self.display)

        # Show countdown text one second before transitioning to final boss
        if progress >= 0.8 and not self.show_warning:
            self.show_warning = True

        if remaining_seconds > 0:
            countdown_text = pygame.font.Font(None, 36).render(f"Final boss in {remaining_seconds} seconds!", True, (255, 255, 255))
            text_rect = countdown_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
            self.display.blit(countdown_text, text_rect)
        else:
            self.gameStateManager.set_state("finalBoss")

        pygame.display.flip()


class finalBossPage:
    """A class which represent the final boss fight page."""
    def prim_run(self):
        pass

    def __init__(self, display, gameStateManager, clock):
        self.selected_option = None
        self.display = display
        self.gameStateManager = gameStateManager
        self.periodNumber = 0
        self.clock = clock

        self.questions_egypt = [
            Question(self.display, "Who was a queen of ancient egypt",
                     ["Cleopatra", "Elizabeth I", "Elizabeth II", "Maria"], 0),
            Question(self.display, "On which years does the ancient egypt control on?",
                     ["154 BCE to 57 BCE", "286 BCE to 10 BCE", "3686 BCE to 1043 BCE", "2686 BCE to 1070 BCE"], 3),
            Question(self.display, "Which pyramid was built before?",
                     ["Pyramid of Khufu", "Pyramid of Khafre", "Pyramid of Djoser", "Pyramid of Menkaure"], 2),
            Question(self.display, "What was the primary purpose of the pyramids in ancient Egypt?",
                     ["Religious temples", "Royal residences", "Tombs for pharaohs", "Military fortifications"], 2),
            Question(self.display, "Which river was crucial to the agricultural success of ancient Egypt?",
                     ["Tigris River", "Nile River", "Euphrates River", "Jordan River"], 1),
            Question(self.display, "The ancient Egyptian writing system is known as:",
                     ["Sanskrit", "Cuneiform", "Calligraphy", "Hieroglyphics"], 3),
        ]

        self.questions_rome = [
            Question(self.display, "Which figure is traditionally credited with the founding of Rome?",
                     ["Julius Caesar", "Romulus", "Augustus", "Hannibal"], 1),
            Question(self.display,
                     "What was the name of the system of the democratic government in ancient Rome?",
                     ["Oligarchy", "Monarchy", "Republic", "Empire"], 2),
            Question(self.display,
                     "Which Carthaginian general famously led an invasion of Italy during the Second Punic War?",
                     ["Nero", "Cleopatra", "Hannibal", "Pompey"], 2),
            Question(self.display,
                     "What architectural feature did ancient Romans innovate and helped build the Colosseum?",
                     ["Domes", "Aqueducts", "Arches", "Stepped pyramids"], 2),
            Question(self.display,
                     "Who was the first Roman emperor who beginning the Roman Empire?",
                     ["Julius Caesar", "Augustus", "Nero", "Trajan"], 1),
            Question(self.display, "Which ancient Roman poet wrote the epic poem 'The Aeneid'?",
                     ["Homer", "Virgil", "Ovid", "Horace"], 1)
        ]

        self.questions_medieval = [
            Question(self.display, "Which event is traditionally considered the beginning of the Middle Ages?",
                     ["Fall of Rome", "Battle of Hastings", "First Crusade", "Signing of the Magna Carta"], 0),
            Question(self.display, "Which medieval king is known for establishing the Carolingian Empire?",
                     ["Charlemagne", "William the Conqueror", "Richard the Lionheart", "Henry VIII"], 0),
            Question(self.display, "Which famous medieval document limited the power of the English monarch?",
                     ["Code of Hammurabi", "Edict of Milan", "Treaty of Verdun", "Magna Carta"], 3),
            Question(self.display, "What was the dominant religion in medieval Europe?",
                     ["Christianity", "Islam", "Buddhism", "Judaism"], 0),
            Question(self.display, "Which event marked the end of the medieval period?",
                     ["Black Death", "Crusades", "Renaissance", "Protestant Reformation"], 2),
            Question(self.display, "Which medieval knightly order was formed during the Crusades?",
                     ["Templars", "Teutonic Knights", "Knights Hospitaller", "Order of the Garter"], 0),
        ]

        self.questions_industrial_revolution = [
            Question(self.display, "In which century did the Industrial Revolution begin?",
                     ["16th century", "17th century", "18th century", "19th century"], 2),
            Question(self.display, "Which country is often considered the birthplace of the Industrial Revolution?",
                     ["France", "Germany", "United States", "United Kingdom"], 3),
            Question(self.display, "Which technological innovation played a central role in the Industrial Revolution?",
                     ["Steam engine", "Printing press", "Compass", "Wheel"], 0),
            Question(self.display,
                     "What major industry experienced significant mechanization during the Industrial Revolution?",
                     ["Agriculture", "Textiles", "Construction", "Transportation"], 1),
            Question(self.display, "Which economic system emerged as a result of the Industrial Revolution?",
                     ["Mercantilism", "Feudalism", "Capitalism", "Socialism"], 2),
            Question(self.display,
                     "What's the name of the movement for better working conditions in the Industrial Revolution?",
                     ["Suffrage Movement", "Civil Rights Movement", "Labor Movement", "Feminist Movement"], 2),
        ]

        self.questions_modern_times = [
            Question(self.display, "In which century did the modern era begin?",
                     ["16th century", "17th century", "18th century", "19th century"], 2),
            Question(self.display, "Which event is often considered the start of the modern age?",
                     ["American Revolution", "French Revolution", "Industrial Revolution", "World War I"], 1),
            Question(self.display,
                     "Which technological advancement had the most significant impact on daily life in the modern era?",
                     ["Internet", "Electricity", "Automobile", "Telephone"], 0),
            Question(self.display, "Which political ideology gained prominence in the 20th century?",
                     ["Feudalism", "Capitalism", "Absolutism", "Mercantilism"], 1),
            Question(self.display, "What major conflict defined the first half of the 20th century?",
                     ["World War I", "Cold War", "Vietnam War", "World War II"], 3),
            Question(self.display,
                     "Which organization was established after WWII to promote peace and cooperation?",
                     ["NATO", "United Nations", "European Union", "ASEAN"], 1),
        ]
        self.questionsList = [self.questions_egypt,
                              self.questions_rome,
                              self.questions_medieval,
                              self.questions_industrial_revolution,
                              self.questions_modern_times]

        # Create QuestionPage instance
        self.question_page = QuestionPage(self.display, self.questions_egypt)
        self.player_attack_animation = AnimatedSprite(PLAYER_ATTACK_FRAMES, 5, (PLAYER_X_POS, PLAYER_Y_POS))
        self.player_idle_animation = AnimatedSprite(PLAYER_IDLE_FRAMES, 5, (PLAYER_X_POS, PLAYER_Y_POS))
        self.current_animation = self.player_idle_animation
        self.playerXpos = PLAYER_X_POS
        self.boss = Boss(self.display, self.periodNumber)

    def run(self):
        # The function get an integer which represent the current period
        # The function blit on the screen all the sprites and the animations of this page

        # The background
        image_object(self.display, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0, 0, BOSS_FIGHT_BACKGROUNDS_LIST[self.periodNumber]).add_on_screen()

        # Render current question
        self.question_page.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.question_page.selected_option = (self.question_page.selected_option - 1) % len(
                        self.question_page.questions[self.question_page.current_question_index].answers)
                elif event.key == pygame.K_DOWN:
                    self.question_page.selected_option = (self.question_page.selected_option + 1) % len(
                        self.question_page.questions[self.question_page.current_question_index].answers)
                elif event.key == pygame.K_RETURN:
                    # Check answer
                    selected_answer_index = self.question_page.selected_option
                    current_question = self.question_page.questions[self.question_page.current_question_index]
                    is_correct = current_question.check_answer(selected_answer_index)

                    # Move to next question if answered
                    if is_correct:
                        if self.question_page.current_question_index >= len(self.question_page.questions) - 1:
                            self.periodNumber += 1

                            # set player positions
                            if self.periodNumber == 1:
                                self.player_idle_animation.rect.center = (self.playerXpos, PLAYER_Y_POS + 30)
                                self.boss.yPos += 30
                            if self.periodNumber == 2:
                                self.player_idle_animation.rect.center = (self.playerXpos, PLAYER_Y_POS + 10)
                                self.boss.yPos -= 20
                            if self.periodNumber == 3:
                                self.player_idle_animation.rect.center = (self.playerXpos, PLAYER_Y_POS - 8)
                                self.boss.yPos -= 8

                            # Set the question title color
                            if 2 <= self.periodNumber <= 3:
                                self.question_page.title_color = (0, 0, 0)
                            else:
                                self.question_page.title_color = (255, 255, 255)
                            self.question_page.questions = self.questionsList[self.periodNumber]
                            self.question_page.current_question_index = 0
                            # TimeAxisPage(self.display, self.gameStateManager, self.periodNumber+1, self.clock).run()

                        else:
                            self.question_page.current_question_index += 1
                        self.current_animation = self.player_attack_animation
                        self.boss.gotHit = 1 # Make the enemy get heart
                        self.player_attack_animation.rect.center = (self.player_attack_animation.rect.center[0] + 200, self.player_attack_animation.rect.center[1])
                        for i in range(100):
                            self.playerXpos += 3
                            self.player_attack_animation.rect.center = (self.playerXpos, PLAYER_Y_POS)
                            self.display.blit(self.current_animation.image, self.current_animation.rect)
                            pygame.display.update()

        self.boss.run()
        for i in range(len(self.current_animation.frames)):
            self.current_animation.update()
            self.display.blit(self.current_animation.image, self.current_animation.rect)
        self.current_animation = self.player_idle_animation
        self.playerXpos = PLAYER_X_POS

        if self.periodNumber >= 5:
            self.gameStateManager.set_state('Certificate')

class CertificatePage:
    """A class of the egypt period."""

    def prim_run(self):
        pass

    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        # The function get nothing
        # The function run all the elements of this page
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        image_object(screen=self.display, width=WINDOW_WIDTH, length=WINDOW_HEIGHT, x_pos=0, y_pos=0, tag_id=0, image_path=CERTIFICATE_IMAGE).add_on_screen()