import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Birthday!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 223, 0)
RED = (255, 0, 0)
PINK = (255, 182, 193)

# Fonts
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 36)

# Cake details
cake_x = width // 2 - 100
cake_y = height // 2
cake_width = 200
cake_height = 100

# Candle details
candle_width = 10
candle_height = 30
flame_radius = 5

# Message
message = "Happy Birthday!"

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw the cake base
    pygame.draw.rect(screen, PINK, (cake_x, cake_y, cake_width, cake_height))
    
    # Draw the candles
    for i in range(3):
        candle_x = cake_x + (i + 1) * (cake_width // 4) - candle_width // 2
        candle_y = cake_y - candle_height
        pygame.draw.rect(screen, BROWN, (candle_x, candle_y, candle_width, candle_height))
        
        # Draw the flame
        flame_x = candle_x + candle_width // 2
        flame_y = candle_y - flame_radius * 2
        pygame.draw.circle(screen, YELLOW, (flame_x, flame_y), flame_radius)
        pygame.draw.circle(screen, RED, (flame_x, flame_y + 2), flame_radius // 2)

    # Display the birthday message
    text_surface = font.render(message, True, BLACK)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 4))

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
