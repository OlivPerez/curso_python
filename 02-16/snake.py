import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fuente
font = pygame.font.SysFont("arial", 20)

# Variables del juego
snake = [(100, 100)]
snake_dir = (BLOCK_SIZE, 0)

food = (random.randrange(0, WIDTH, BLOCK_SIZE),
        random.randrange(0, HEIGHT, BLOCK_SIZE))

score = 0
high_score = 0


def draw_text(text, x, y, align="left"):
    render = font.render(text, True, WHITE)
    rect = render.get_rect()
    if align == "right":
        rect.topright = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(render, rect)


def reset_game():
    global snake, snake_dir, food, score
    snake = [(100, 100)]
    snake_dir = (BLOCK_SIZE, 0)
    food = (random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE))
    score = 0


# Bucle principal
running = True
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                snake_dir = (0, -BLOCK_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                snake_dir = (0, BLOCK_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                snake_dir = (-BLOCK_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                snake_dir = (BLOCK_SIZE, 0)

    # Mover serpiente
    head_x = snake[0][0] + snake_dir[0]
    head_y = snake[0][1] + snake_dir[1]
    new_head = (head_x, head_y)

    # Colisiones con bordes o consigo misma
    if (head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake):
        high_score = max(high_score, score)
        reset_game()
        continue

    snake.insert(0, new_head)

    # Comer comida
    if new_head == food:
        score += 1
        if score > high_score:
            high_score = score
        food = (random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE))
    else:
        snake.pop()

    # Dibujar
    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                         (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, RED,
                     (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Mostrar puntuaciones
    draw_text(f"Puntuación: {score}", 10, 10, "left")
    draw_text(f"Puntuación Máxima: {high_score}", WIDTH - 10, 10, "right")

    pygame.display.update()

pygame.quit()
sys.exit()
