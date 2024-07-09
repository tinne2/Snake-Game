import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

font = pygame.font.SysFont(None, 35)

def draw_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

def get_random_food_position(snake):
    while True:
        position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if position not in snake:
            return position

def game_loop():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = 'right'
    snake_speed = 5
    score = 0

    food = get_random_food_position(snake)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != 'down':
                    snake_direction = 'up'
                elif event.key == pygame.K_DOWN and snake_direction != 'up':
                    snake_direction = 'down'
                elif event.key == pygame.K_LEFT and snake_direction != 'right':
                    snake_direction = 'left'
                elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                    snake_direction = 'right'

        x, y = snake[0]
        if snake_direction == 'up':
            y -= 1
        elif snake_direction == 'down':
            y += 1
        elif snake_direction == 'left':
            x -= 1
        elif snake_direction == 'right':
            x += 1

        if (x, y) == food:
            snake.append(snake[-1])
            food = get_random_food_position(snake)
            score += 1
            snake_speed += 1

        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT or (x, y) in snake[1:]:
            break

        snake = [(x, y)] + snake[:-1]

        screen.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.flip()

        clock.tick(snake_speed)

    return score

def main():
    while True:
        score = game_loop()
        screen.fill(BLACK)
        draw_text(f"Game Over! Score: {score}", RED, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 20)
        draw_text("Press any key to play again", WHITE, SCREEN_WIDTH // 4 - 30, SCREEN_HEIGHT // 2 + 20)
        pygame.display.flip()
        wait_for_key()

def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return

if __name__ == "__main__":
    main()
