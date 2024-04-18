import pygame.sprite
import sys
import os
from pathlib import Path

from Classes.Game import *
from Classes.Image_Object import *
from constants import *
from Classes.AnimatedSprite import *
from Classes.Button import *
from Classes.MovingTextAnimation import *
from Classes.Question import *
from Classes.Boss import *
from Classes.Slider import *

class HomePage:
    """A class of the home page."""

    def __init__(self, display, gameStateManager, clock):
        self.display = display
        self.gameStateManager = gameStateManager
        self.clock = clock

    def prim_run(self):
        pygame.mixer.music.load(HOMEPAGE_BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1)

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
                    self.gameStateManager.set_state("Settings")
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

                            if self.periodNumber <= 4:
                                self.question_page.questions = self.questionsList[self.periodNumber]
                                self.question_page.current_question_index = 0
                                # TimeAxisPage(self.display, self.gameStateManager, self.periodNumber+1, self.clock).run()

                            else:
                                self.gameStateManager.set_state('Certificate')

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

class CertificatePage:
    """A class of the egypt period."""

    def prim_run(self):
        pass

    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.username = ""
        self.saveButtonPos = (WINDOW_WIDTH // 2, 500)
        self.isGotName = False

    def GetName(self):
        image_object(screen=self.display, width=WINDOW_WIDTH, length=WINDOW_HEIGHT, x_pos=0, y_pos=0, tag_id=0,
                     image_path=BG2).add_on_screen()

        # A tuple of (x, y) which indicate the mouse position
        menu_mouse_pos = pygame.mouse.get_pos()

        save_button = Button(None, pos=self.saveButtonPos, text_input="SAVE", font=pygame.font.Font(FONT2, 20),
                             base_color="#d7fcd4", hovering_color="White")
        save_button.changeColor(menu_mouse_pos)
        save_button.update(self.display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                elif event.key == pygame.K_RETURN:
                    # Do something with the entered name, for example, print it
                    print("Entered Name:", WINDOW_WIDTH // 2, 500)
                    text = ""
                else:
                    self.username += event.unicode
            elif save_button.checkForInput(menu_mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True

        # Render the title
        title_surface = pygame.font.Font(FONT2, 25).render("Your name:", True, BLACK)
        title_rect = title_surface.get_rect(midleft=(50, WINDOW_HEIGHT / 2))
        self.display.blit(title_surface, title_rect)

        # Render the text input bar
        input_bar_rect = pygame.Rect(title_rect.right + 10, WINDOW_HEIGHT / 2 - 25 / 2, 250, 25)
        pygame.draw.rect(self.display, BLACK, input_bar_rect, 2)

        # Render the text
        text_surface = pygame.font.Font(FONT2, 15).render(self.username, True, BLACK)
        text_rect = text_surface.get_rect(midleft=(title_rect.right + 15, WINDOW_HEIGHT / 2))

        # Ensure the text stays within the input bar
        if text_rect.width > input_bar_rect.width:
            self.username = self.username[:-1]
        self.display.blit(text_surface, text_rect)
        pygame.display.flip()
        return False

    def run(self):
        # The function get nothing
        # The function run all the elements of this page

        # A tuple of (x, y) which indicate the mouse position
        menu_mouse_pos = pygame.mouse.get_pos()

        if not self.isGotName:
            self.isGotName = self.GetName()

        else:
            image_object(screen=self.display, width=WINDOW_WIDTH, length=WINDOW_HEIGHT, x_pos=0, y_pos=0, tag_id=0,
                         image_path=CERTIFICATE_IMAGE).add_on_screen()
            # Render username
            title_surface = pygame.font.Font(FONT2, 25).render(self.username, True, (255, 255, 255))
            title_rect = title_surface.get_rect(midleft=(550, WINDOW_HEIGHT / 2))
            self.display.blit(title_surface, title_rect)
            download_button = Button(None, pos=(WINDOW_WIDTH // 2, 550), text_input="Download", font=pygame.font.Font(FONT2, 20), base_color="#d7fcd4", hovering_color="White")

            download_button.changeColor(menu_mouse_pos)
            download_button.update(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif download_button.checkForInput(menu_mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Get the path to the user's desktop
                        desktop_path = Path.home() / "Desktop"

                        # Create the folder if it doesn't exist
                        if not desktop_path.exists():
                            desktop_path.mkdir()

                        # Capture the screen contents
                        pygame.image.save(self.display, str(desktop_path / "game_certificate.png"))

                        print("The file got saved on desktop")

class Settings:

    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.audio_slider = Slider(WINDOW_WIDTH // 3.5, 215, 400)
        self.brightness_slider = Slider(WINDOW_WIDTH // 3.5, 315, 400)

    def prim_run(self):
        pass

    def run(self):
        # The function get nothing
        # The function run all the elements of this page

        # The background
        self.display.blit(HOMEPAGE_BACKGROUND_IMG, (0, 0))

        # A tuple of (x, y) which indicate the mouse position
        menu_mouse_pos = pygame.mouse.get_pos()

        #Logos
        audio_text = pygame.font.Font(FONT2, 20).render("AUDIO", True, "#ffffff")
        audio_rect = audio_text.get_rect(center=(WINDOW_WIDTH // 2, 200))
        self.display.blit(audio_text, audio_rect)


        brightness_text = pygame.font.Font(FONT2, 20).render("BRIGHTNESS", True, "#ffffff")
        brightness_rect = brightness_text.get_rect(center=(WINDOW_WIDTH // 2, 300))
        self.display.blit(brightness_text, brightness_rect)



        # The main title
        menu_text = pygame.font.Font(FONT2, 40).render("SETTINGS", True, "#ffffff")
        menu_rect = menu_text.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.display.blit(menu_text, menu_rect)




        # The buttons
        apply_button = Button(None, pos=(WINDOW_WIDTH // 2, 425), text_input="APPLY", font=pygame.font.Font(FONT2, 30), base_color="#d7fcd4", hovering_color="White")


        # Changing the font color while holding on the button
        for button in [apply_button]:
            button.changeColor(menu_mouse_pos)
            button.update(self.display)

        # Checking for mouse click on the buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button pressed
                    if apply_button.checkForInput(menu_mouse_pos):
                        pygame.mixer.music.set_volume(self.audio_slider.get_value())  # Adjust volume level as needed
                        self.gameStateManager.set_state('Home')
                    if self.audio_slider.checkForInput(menu_mouse_pos):
                        self.audio_slider.is_dragging = True
                    if self.brightness_slider.checkForInput(menu_mouse_pos):
                        self.brightness_slider.is_dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button released
                    self.audio_slider.is_dragging = False
                    self.brightness_slider.is_dragging = False

            if event.type == pygame.MOUSEMOTION:
                menu_mouse_pos = pygame.mouse.get_pos()  # Update mouse position
                if self.audio_slider.is_dragging:  # Slider is being dragged
                    self.audio_slider.update_value(menu_mouse_pos[0])
                if self.brightness_slider.is_dragging:  # Slider is being dragged
                    self.brightness_slider.update_value(menu_mouse_pos[0])


        self.audio_slider.draw(self.display)
        self.brightness_slider.draw(self.display)