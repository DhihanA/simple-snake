import pygame
import sys
from snake import *
from food import Food


def main():
    pygame.init()
    bounds = (500,500)
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Snake")

    block_size = 20
    snake = Snake(block_size, bounds)
    food = Food(block_size, bounds)
    font = pygame.font.SysFont('comicsans',20, True)
    delay = 100

    run = True
    while run:
        if snake.length >= 10:
            delay = 75
        pygame.time.delay(delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.steer(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            snake.steer(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            snake.steer(Direction.UP)
        elif keys[pygame.K_DOWN]:
            snake.steer(Direction.DOWN)
        snake.move()
        snake.check_for_food(food)

        if snake.check_tail_collision() == True:
            text = font.render('Game Over! Hit spacebar!', True, (255,255,255))
            window.blit(text, (125, 200))
            pygame.display.update()

            space_pressed = False
            while not space_pressed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        space_pressed = True

                pygame.time.delay(100)
            
            snake.respawn()
            food.respawn()


        window.fill((0,0,0))
        snake.draw(pygame, window)
        food.draw(pygame, window)
        pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()