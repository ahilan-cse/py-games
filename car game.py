import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Car dimensions
CAR_WIDTH = 50
CAR_HEIGHT = 100

# Load car images (player and enemy)
player_car = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
player_car.fill(GREEN)
enemy_car = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
enemy_car.fill(RED)

# Player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - CAR_HEIGHT - 20
player_speed = 5

# Enemy car list
enemy_cars = []
enemy_speed = 5
enemy_spawn_timer = 0
enemy_spawn_delay = 30

# Game variables
clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.Font(None, 36)

# Function to display text on the screen
def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Main game loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - CAR_WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - CAR_HEIGHT:
        player_y += player_speed

    # Spawn enemy cars
    enemy_spawn_timer += 1
    if enemy_spawn_timer > enemy_spawn_delay:
        enemy_x = random.randint(0, SCREEN_WIDTH - CAR_WIDTH)
        enemy_cars.append([enemy_x, -CAR_HEIGHT])
        enemy_spawn_timer = 0

    # Move enemy cars
    for enemy in enemy_cars[:]:
        enemy[1] += enemy_speed
        if enemy[1] > SCREEN_HEIGHT:
            enemy_cars.remove(enemy)
            score += 1

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
    for enemy in enemy_cars:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], CAR_WIDTH, CAR_HEIGHT)
        if player_rect.colliderect(enemy_rect):
            running = False  # Game over on collision

    # Draw player car
    screen.blit(player_car, (player_x, player_y))

    # Draw enemy cars
    for enemy in enemy_cars:
        screen.blit(enemy_car, (enemy[0], enemy[1]))

    # Display score
    display_text(f"Score: {score}", 10, 10)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# End of game
display_text("Game Over!", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2)
pygame.display.flip()
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()

