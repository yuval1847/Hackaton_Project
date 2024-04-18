import pygame
from constants import *

class Question:
    def __init__(self, display, question_text, answers, correct_answer_index):
        """
        Initialize a question object.

        display: screen, the display of the game
        question_text: str, the text of the question
        answers: list of str, the possible answers
        correct_answer_index: int, the index of the correct answer in the answers list
        """
        self.display = display
        self.question_text = question_text
        self.answers = answers
        self.correct_answer_index = correct_answer_index

    def check_answer(self, selected_answer_index):
        """
        Check if the provided answer index matches the correct answer.

        selected_answer_index: int, the index of the selected answer
        bool, True if the selected answer is correct, False otherwise
        """
        return selected_answer_index == self.correct_answer_index

class QuestionPage:
    """A class which represent a page of questions."""

    def __init__(self, display, questions):
        self.display = display
        self.font = pygame.font.Font(FONT3, 30)  # Choose your font and size
        self.questions = questions
        self.current_question_index = 0
        self.selected_option = 0  # Index of the selected option
        self.title_color = (255, 255, 255)

    def render(self):
        question = self.questions[self.current_question_index]

        # Render question text
        question_text = self.font.render(question.question_text, True, self.title_color)  # White color
        question_rect = question_text.get_rect(center=(self.display.get_width() // 2, 75))

        # Render the options
        max_option_width = max([self.font.size(option)[0] for option in question.answers])
        option_height = self.font.get_height()
        padding = 20
        total_height = (len(question.answers) + 1) * option_height + padding * 2
        rect_y = (self.display.get_height() - total_height) // 2
        pygame.draw.rect(self.display, (255, 255, 255), (QUESTION_RECT_X_POS, QUESTION_RECT_Y_POS, max_option_width + padding * 2, total_height))

        pygame.draw.rect(self.display, (255, 255, 255), question_rect, 2)  # White rectangle around question
        self.display.blit(question_text, question_rect)

        # Render the options
        for i, option in enumerate(question.answers):
            option_text = self.font.render(option, True, (0, 0, 0))  # Black color
            option_rect = option_text.get_rect(x=20, y=QUESTION_RECT_Y_POS + 20 + QUESTION_RECT_X_POS + i * option_height)
            if i == self.selected_option:
                pygame.draw.rect(self.display, (255, 0, 0), option_rect, 2)  # Highlight selected option
            self.display.blit(option_text, option_rect)