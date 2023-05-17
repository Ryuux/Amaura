import pygame
from constants import RED, BLOCK_SIZE, WIDTH, HEIGHT
import random

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.generate()

    def generate(self):
        x = random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE
        y = random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.position = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))
