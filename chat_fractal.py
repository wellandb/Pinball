# Importing necessary modules
import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the color
color = (0, 228, 137)

# Define the function to draw the fractal
def draw_fractal(x, y, size, depth, angle):
    if depth > 0:
        # Draw the irregular shape
        points = [(x + size * math.cos(angle), y + size * math.sin(angle)),
                  (x + size * math.cos(angle + math.pi / 2), y + size * math.sin(angle + math.pi / 2)),
                  (x + size * math.cos(angle + math.pi), y + size * math.sin(angle + math.pi)),
                  (x + size * math.cos(angle + 3 * math.pi / 2), y + size * math.sin(angle + 3 * math.pi / 2))]
        pygame.draw.polygon(screen, color, points)

        # Recursively draw the fractal
        draw_fractal(x + size * math.cos(angle), y + size * math.sin(angle), size / 1.15, depth - 1, angle + 4.448864235759929)
        draw_fractal(x + size * math.cos(angle + math.pi / 2), y + size * math.sin(angle + math.pi / 2), size / 1.15, depth - 1, angle + 4.448864235759929)
        draw_fractal(x + size * math.cos(angle + math.pi), y + size * math.sin(angle + math.pi), size / 1.15, depth - 1, angle + 4.448864235759929)
        draw_fractal(x + size * math.cos(angle + 3 * math.pi / 2), y + size * math.sin(angle + 3 * math.pi / 2), size / 1.15, depth - 1, angle + 4.448864235759929)

# Call the function to draw the fractal
draw_fractal(screen_width / 2, screen_height / 2, 200, 1, 0)

# Update the screen
pygame.display.update()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
