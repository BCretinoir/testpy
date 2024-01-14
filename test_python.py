import pygame
import sys
import random

def drawFood():
    foodColor = pygame.Color("red")   
    food_rect = pygame.Rect(food[0] * grid_w, food[1] * grid_h, grid_w, grid_h)
    pygame.draw.rect(wind, foodColor, food_rect)

def drawSnake():
    snakeColor = pygame.Color("white")
    for pos in snake:
        snake_rect = pygame.Rect(pos[0] * grid_w, pos[1] * grid_h, grid_w, grid_h)
        pygame.draw.rect(wind, snakeColor, snake_rect)

def updateSnake(direction):
    global food
    global running
    dirX, dirY = direction    
    head = snake[0].copy()
    head[0] = (head[0] + dirX) % grid_x
    head[1] = (head[1] + dirY) % grid_y

    if head in snake[1:]:
        running = False
    elif head == food:
        while True:
            newfood = [
                random.randint(0, grid_x - 1),
                random.randint(0, grid_y - 1)
            ]
            if newfood not in snake:
                break
        food = newfood
        snake.insert(0, head)
    else:
        snake.pop()
        snake.insert(0, head)

# Ouvrir la fenêtre avec Pygame
pygame.init()
wind = pygame.display.set_mode((1280, 960))

backgroundColor = pygame.Color("black")

## Découpage de l'écran / grille

grid_x = 32
grid_y = 24

grid_w = wind.get_width() // grid_x
grid_h = wind.get_height() // grid_y

## Définir le serpent 

snk_x, snk_y = grid_x // 4, grid_y // 2
snake = [
    [snk_x, snk_y],
    [snk_x-1, snk_y],
    [snk_x-2, snk_y],
]

## Définir la nourriture

food = [grid_x // 2, grid_y // 2]

# Boucle de jeu 
running = True
direction = [1, 0]
opposite_direction = [-1, 0]
while running:
    pygame.time.Clock().tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RIGHT and not direction == [-1, 0]:  # fleche droite
                direction = [1, 0]
            elif event.key == pygame.K_LEFT and not direction == [1, 0]:  # fleche gauche
                direction = [-1, 0]
            elif event.key == pygame.K_UP and not direction == [0, 1]:  # fleche haut
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and not direction == [0, -1]:  # fleche bas
                direction = [0, 1] 

    # Mise à jour de la position du serpent
    updateSnake(direction)

    # Dessiner
    wind.fill(backgroundColor)
    drawFood()
    drawSnake()

    pygame.display.update()

pygame.quit()
sys.exit()
