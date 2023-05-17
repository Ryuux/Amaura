import pygame
from constants import GREEN, BLOCK_SIZE, WIDTH, HEIGHT

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = pygame.K_RIGHT

    def move(self):
        x, y = self.body[0]
        if self.direction == pygame.K_UP:
            y -= BLOCK_SIZE
        elif self.direction == pygame.K_DOWN:
            y += BLOCK_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= BLOCK_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += BLOCK_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        opposite_directions = {pygame.K_UP: pygame.K_DOWN, pygame.K_DOWN: pygame.K_UP,
                               pygame.K_LEFT: pygame.K_RIGHT, pygame.K_RIGHT: pygame.K_LEFT}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self):
        if self.body[0] in self.body[1:]:
            return True
        if not (0 <= self.body[0][0] < WIDTH and 0 <= self.body[0][1] < HEIGHT):
            return True
        return False

    def eat(self, food_position):
        return self.body[0] == food_position

    def grow(self):
        last_segment = self.body[-1]
        x, y = last_segment
        if self.direction == pygame.K_UP:
            y += BLOCK_SIZE
        elif self.direction == pygame.K_DOWN:
            y -= BLOCK_SIZE
        elif self.direction == pygame.K_LEFT:
            x += BLOCK_SIZE
        elif self.direction == pygame.K_RIGHT:
            x -= BLOCK_SIZE
        self.body.append((x, y))