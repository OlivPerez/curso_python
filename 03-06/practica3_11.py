import pygame
import random

# --- Configuración ---
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 32
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE

BLACK = (0,0,0)
WHITE = (200,200,200)
GREEN = (0,200,0)
RED = (200,0,0)
BLUE = (0,0,200)
YELLOW = (255,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# --- Generar sala ---
def generar_sala(rows, cols, num_enemigos=5):
    grid = [[1 for _ in range(cols)] for _ in range(rows)]
    for r in range(2, rows-2):
        for c in range(2, cols-2):
            grid[r][c] = 0
    enemigos = []
    for _ in range(num_enemigos):
        while True:
            ex, ey = random.randint(3, rows-4), random.randint(3, cols-4)
            if grid[ex][ey] == 0:
                tipo = random.choice(["random","chaser"])
                enemigos.append({"pos":[ex, ey], "tipo":tipo})
                break
    return grid, enemigos

# --- Estado inicial ---
sala, enemigos = generar_sala(ROWS, COLS)
player_pos = [ROWS//2, COLS//2]
puerta = None
proyectiles = []
game_over = False

# Cadencia de disparo
last_shot_time = 0
shot_delay = 300  # ms

# Cadencia de movimiento jugador
last_move_time = 0
move_delay = 150  # ms

# Cadencia de movimiento enemigos
last_enemy_move_time = 0
enemy_move_delay = 500  # ms

# --- Loop principal ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    if not game_over:
        # Movimiento del jugador con cooldown
        if current_time - last_move_time > move_delay:
            dx, dy = 0, 0
            if keys[pygame.K_UP]: dx, dy = -1, 0
            if keys[pygame.K_DOWN]: dx, dy = 1, 0
            if keys[pygame.K_LEFT]: dx, dy = 0, -1
            if keys[pygame.K_RIGHT]: dx, dy = 0, 1

            nx, ny = player_pos[0]+dx, player_pos[1]+dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and sala[nx][ny] == 0:
                player_pos = [nx, ny]
                last_move_time = current_time

        # Disparos con WASD
        if current_time - last_shot_time > shot_delay:
            if keys[pygame.K_a]:
                proyectiles.append([player_pos[0], player_pos[1], 0, -1])
                last_shot_time = current_time
            elif keys[pygame.K_d]:
                proyectiles.append([player_pos[0], player_pos[1], 0, 1])
                last_shot_time = current_time
            elif keys[pygame.K_w]:
                proyectiles.append([player_pos[0], player_pos[1], -1, 0])
                last_shot_time = current_time
            elif keys[pygame.K_s]:
                proyectiles.append([player_pos[0], player_pos[1], 1, 0])
                last_shot_time = current_time

        # Mover proyectiles
        nuevos_proyectiles = []
        for px, py, dx, dy in proyectiles:
            nx, ny = px+dx, py+dy
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if sala[nx][ny] == 1:
                    continue
                impacto = False
                for enemigo in enemigos[:]:
                    if enemigo["pos"] == [nx, ny]:
                        enemigos.remove(enemigo)
                        impacto = True
                        break
                if not impacto:
                    nuevos_proyectiles.append([nx, ny, dx, dy])
        proyectiles = nuevos_proyectiles

        # Movimiento de enemigos con cooldown
        if current_time - last_enemy_move_time > enemy_move_delay:
            for enemigo in enemigos:
                ex, ey = enemigo["pos"]
                if enemigo["tipo"] == "random":
                    dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1),(0,0)])
                else:  # chaser
                    dx = 0
                    dy = 0
                    if ex < player_pos[0]: dx = 1
                    elif ex > player_pos[0]: dx = -1
                    if ey < player_pos[1]: dy = 1
                    elif ey > player_pos[1]: dy = -1
                nx, ny = ex+dx, ey+dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and sala[nx][ny] == 0:
                    enemigo["pos"] = [nx, ny]
            last_enemy_move_time = current_time

        # Colisiones con enemigos → Game Over
        for enemigo in enemigos:
            if enemigo["pos"] == player_pos:
                game_over = True

        # Si no quedan enemigos, aparece una puerta
        if not enemigos and puerta is None:
            lado = random.choice(["top","bottom","left","right"])
            if lado == "top":
                puerta = ("top", [1, COLS//2])
            elif lado == "bottom":
                puerta = ("bottom", [ROWS-2, COLS//2])
            elif lado == "left":
                puerta = ("left", [ROWS//2, 1])
            elif lado == "right":
                puerta = ("right", [ROWS//2, COLS-2])
            sala[puerta[1][0]][puerta[1][1]] = 0

        # Si el jugador entra en la puerta → nueva sala
        if puerta and player_pos == puerta[1]:
            sala, enemigos = generar_sala(ROWS, COLS)
            lado = puerta[0]
            if lado == "top":
                player_pos = [ROWS-3, COLS//2]
            elif lado == "bottom":
                player_pos = [2, COLS//2]
            elif lado == "left":
                player_pos = [ROWS//2, COLS-3]
            elif lado == "right":
                player_pos = [ROWS//2, 2]
            puerta = None
            proyectiles = []

    # --- Dibujar ---
    screen.fill(BLACK)
    for r in range(ROWS):
        for c in range(COLS):
            if sala[r][c] == 0:
                pygame.draw.rect(screen, WHITE, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # jugador
    pygame.draw.rect(screen, GREEN, (player_pos[1]*TILE_SIZE, player_pos[0]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # enemigos
    for enemigo in enemigos:
        ex, ey = enemigo["pos"]
        color = RED if enemigo["tipo"] == "random" else (255,100,100)  # chasers más claros
        pygame.draw.rect(screen, color, (ey*TILE_SIZE, ex*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # puerta
    if puerta:
        pygame.draw.rect(screen, BLUE, (puerta[1][1]*TILE_SIZE, puerta[1][0]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # proyectiles
    for px, py, _, _ in proyectiles:
        pygame.draw.rect(screen, YELLOW, (py*TILE_SIZE, px*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # game over
    if game_over:
        text = font.render("GAME OVER - R para reiniciar", True, RED)
        screen.blit(text, (WIDTH//2-200, HEIGHT//2-20))
        if keys[pygame.K_r]:
            sala, enemigos = generar_sala(ROWS, COLS)
            player_pos = [ROWS//2, COLS//2]
            puerta = None
            proyectiles = []
            game_over = False
            last_shot_time = 0
            last_move_time = 0
            last_enemy_move_time = 0

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
