import pygame
from constants import *

class AnimatedSprite(pygame.sprite.Sprite):
    """A class which represent an animation of sprites(frames)."""

    def __init__(self, frames, frame_duration, pos):
        super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.frame_duration = frame_duration
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_duration:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
        return self.image