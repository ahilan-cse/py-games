import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Object")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Basket settings
basket_width, basket_height = 100, 20
basket_x = (screen_width - basket_width) / 2
basket_y = screen_height - basket_height - 10
basket_speed = 10

# Falling object settings
object_width, object_height = 30, 30
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height
object_speed = 5

# Score settings
score = 0
font = pygame.font.Font(None, 36)

# Game loop control
running = True

# Main game loop
while running:
    # Fill screen with white
    screen.fill(white)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    # Move the falling object
    object_y += object_speed

    # Check if the object reaches the bottom of the screen
    if object_y > screen_height:
        # Reset object to the top of the screen at a new random x position
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height

    # Check for collision
    if (basket_x < object_x < basket_x + basket_width or basket_x < object_x + object_width < basket_x + basket_width) and basket_y < object_y + object_height < basket_y + basket_height:
        score += 1
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height

    # Draw the basket
    pygame.draw.rect(screen, blue, (basket_x, basket_y, basket_width, basket_height))

    # Draw the falling object
    pygame.draw.rect(screen, red, (object_x, object_y, object_width, object_height))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Delay to control frame rate
    pygame.time.delay(30)
