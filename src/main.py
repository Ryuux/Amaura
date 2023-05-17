import pygame
from entities.snake import Snake
from entities.food import Food
from constants import BLACK, WIDTH, HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Amaura')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(pygame.K_DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(pygame.K_LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(pygame.K_RIGHT)

    def update(self):
        self.snake.move()

        if self.snake.eat(self.food.position):
            self.snake.grow()
            self.food.generate()
            self.score += 1

        if self.snake.check_collision():
            self.running = False

    def draw(self):
        self.window.fill(BLACK)
        self.snake.draw(self.window)
        self.food.draw(self.window)
        score_text = pygame.font.Font(None, 36).render("Score: " + str(self.score), True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()