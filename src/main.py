import pygame
from entities.snake import Snake
from entities.food import Food
from constants import BLACK, WIDTH, HEIGHT


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Amaura')

clock = pygame.time.Clock()

snake = Snake()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(pygame.K_UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(pygame.K_DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(pygame.K_LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(pygame.K_RIGHT)

    snake.move()

    if snake.eat(food.position):
        snake.grow()
        food.generate()

    if snake.check_collision():
        running = False

    window.fill(BLACK)
    snake.draw(window)
    food.draw(window)
    pygame.display.flip()

    clock.tick(10)  

pygame.quit()
