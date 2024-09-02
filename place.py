import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("r/place-like Canvas")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Pixel grid dimensions
PIXELS_PER_SIDE = 50
PIXEL_SIZE = WIDTH // PIXELS_PER_SIDE

# Create pixel grid
pixels = [[random.choice([WHITE, BLACK]) for _ in range(PIXELS_PER_SIDE)] for _ in range(PIXELS_PER_SIDE)]

# Game loop
running = True
last_change_time = time.time()
cooldown_period = 0.1  # seconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.time()
    
    # Check for pixel changes
    for row in range(PIXELS_PER_SIDE):
        for col in range(PIXELS_PER_SIDE):
            if current_time - last_change_time > cooldown_period:
                pixels[row][col] = random.choice([WHITE, BLACK])
                last_change_time = current_time
    
    # Draw the canvas
    screen.fill(BLACK)
    for row in range(PIXELS_PER_SIDE):
        for col in range(PIXELS_PER_SIDE):
            color = pixels[row][col]
            pygame.draw.rect(screen, color, (col * PIXEL_SIZE, row * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    
    pygame.display.flip()

    # Limit to 60 frames per second
    pygame.time.Clock().tick(60)

pygame.quit()
